"""Manim: the honest die — one chi-squared trial worked in full, then a thousand.

Part 1 (one trial): a fair die is rolled 60 times, live, into a six-bar tally
against the expected 10 per face. Then the table is built row by row —
face, O, O-10, (O-10)^2/10 — and summed to X^2. That number drops as a brick
onto the X^2 axis: one honest experiment, one misfit.
Part 2 (many trials): the same again, and again — first singly, then in
accelerating batches to 100 and 1000 — until the pile of honest misfits IS
Pearson's chi^2_5 curve, which is then drawn over it. The 5% cut at 11.07
lands last, with the fraction of honest dice that fell beyond it.

Date-seeded, like sampling-clt-live.py: rerun on another day and every roll
changes; the curve does not.

Render (from this folder):
    VAULT_DATE=YYYY-MM-DD manim -qm chi-squared-honest-die.py ChiSquaredHonestDie   # smoke
    VAULT_DATE=YYYY-MM-DD manim -qk chi-squared-honest-die.py ChiSquaredHonestDie   # 4K final
(Defaults to the committed date if VAULT_DATE is unset.)
Copy media/videos/chi-squared-honest-die/2160p60/ChiSquaredHonestDie.mp4
  -> chi-squared-honest-die.mp4 beside the card, then rm -rf media/ __pycache__/.
"""

import os
import numpy as np
from scipy import stats
from manim import (
    Scene, VGroup, Axes, Text, MathTex, Rectangle, DashedLine, Line,
    Integer, FadeIn, FadeOut, Transform, ReplacementTransform,
    Create, Write, UP, DOWN, LEFT, RIGHT, UR, config,
)

BG = "#1e1e1e"
TXT = "#cccccc"
GREY = "#9a9a9a"
BLUE = "#2563eb"
PURPLE = "#7c3aed"
AMBER = "#f59e0b"
FONT = "Helvetica Neue"

config.background_color = BG

DATE = os.environ.get("VAULT_DATE", "2026-08-18")
SEED = int(DATE.replace("-", ""))

ROLLS = 60          # rolls per experiment
E = ROLLS / 6       # expected per face = 10
N_TRIALS = 1000
NU = 5
CRIT = float(stats.chi2.ppf(0.95, NU))   # 11.07

BIN_LO, BIN_HI, BIN_W = 0.0, 20.0, 1.0
N_BINS = int((BIN_HI - BIN_LO) / BIN_W)

# table geometry (upper right)
COL_X = [0.8, 1.65, 2.5, 4.2]        # face | O | O-10 | (O-10)^2/10
HEAD_Y, LINE_Y, ROW_Y1, ROW_DY = 2.52, 2.27, 2.02, 0.32   # header, rule, first data row, spacing


class ChiSquaredHonestDie(Scene):
    # ------------------------------------------------------------ helpers
    def swap_caption(self, text, color=TXT, font_size=24):
        cap = Text(text, font=FONT, font_size=font_size, color=color,
                   line_spacing=0.85).to_edge(DOWN, buff=0.2)
        if getattr(self, "_cap", None) is not None:
            self.play(FadeOut(self._cap, run_time=0.2), FadeIn(cap, run_time=0.3))
        else:
            self.play(FadeIn(cap, run_time=0.3))
        self._cap = cap

    def tally_bars(self, counts, color=BLUE):
        g = VGroup()
        for f in range(6):
            x0, x1 = f + 0.62, f + 1.38
            p0 = self.tax.c2p(x0, 0)
            p1 = self.tax.c2p(x1, max(counts[f], 0.001))
            r = Rectangle(width=p1[0] - p0[0], height=p1[1] - p0[1],
                          fill_color=color, fill_opacity=0.55,
                          stroke_color=color, stroke_width=1.5)
            r.move_to((p0 + p1) / 2)
            g.add(r)
        return g

    def olabels_for(self, c):
        return VGroup(*[Text(str(int(c[f])), font=FONT, font_size=20, color=BLUE)
                        .next_to(self.tax.c2p(f + 1, c[f]), UP, buff=0.06) for f in range(6)])

    def swap_olabels(self, c):
        """Return the animations that replace the count labels (no glyph morphing)."""
        new = self.olabels_for(c)
        anims = [FadeOut(self.olabels, run_time=0.25), FadeIn(new, run_time=0.25)]
        self.olabels = new
        return anims

    def hist_bars(self, bincounts, unit):
        """unit = axis-height per count (the y-axis runs 0..1)."""
        g = VGroup()
        for b in range(N_BINS):
            c = bincounts[b]
            if c == 0:
                continue
            x0 = BIN_LO + b * BIN_W
            p0 = self.hax.c2p(x0, 0)
            p1 = self.hax.c2p(x0 + BIN_W, min(c * unit, 1.0))
            r = Rectangle(width=p1[0] - p0[0], height=p1[1] - p0[1],
                          fill_color=BLUE, fill_opacity=0.6,
                          stroke_color=BLUE, stroke_width=1.0)
            r.move_to((p0 + p1) / 2)
            g.add(r)
        return g

    def brick(self, b, level, unit):
        x0 = BIN_LO + b * BIN_W
        p0 = self.hax.c2p(x0, level * unit)
        p1 = self.hax.c2p(x0 + BIN_W, (level + 1) * unit)
        r = Rectangle(width=p1[0] - p0[0], height=p1[1] - p0[1],
                      fill_color=BLUE, fill_opacity=0.6,
                      stroke_color=BLUE, stroke_width=1.0)
        r.move_to((p0 + p1) / 2)
        return r

    @staticmethod
    def bin_of(x):
        return min(N_BINS - 1, max(0, int((x - BIN_LO) / BIN_W)))

    @staticmethod
    def row(cells, y, colors):
        g = VGroup()
        for tex, x, col in zip(cells, COL_X, colors):
            m = MathTex(tex, color=col).scale(0.62).move_to([x, y, 0])
            g.add(m)
        return g

    # ------------------------------------------------------------ scene
    def construct(self):
        rng = np.random.default_rng(SEED)
        faces = rng.integers(1, 7, size=(N_TRIALS, ROLLS))
        counts_all = np.stack([(faces == f).sum(axis=1) for f in range(1, 7)], axis=1)
        X2_all = ((counts_all - E) ** 2 / E).sum(axis=1)

        title = Text("the honest die: how much does a FAIR die misfit its own expectation?",
                     font=FONT, font_size=30, color=TXT).to_edge(UP, buff=0.26)
        stamp = Text(f"date generated: {DATE}  ·  seed = {SEED}", font=FONT,
                     font_size=16, color=GREY).to_corner(UR, buff=0.28).shift(DOWN * 0.5)
        self.play(Write(title), FadeIn(stamp), run_time=1.2)

        # ---- tally panel (upper left)
        self.tax = Axes(x_range=[0.5, 6.5, 1], y_range=[0, 20, 5],
                        x_length=4.3, y_length=2.3,
                        axis_config=dict(color=GREY, stroke_width=2, include_ticks=False,
                                         include_tip=False),
                        ).move_to([-4.55, 1.3, 0])
        face_labels = VGroup(*[Text(str(f), font=FONT, font_size=20, color=TXT)
                               .next_to(self.tax.c2p(f, 0), DOWN, buff=0.1) for f in range(1, 7)])
        eline = DashedLine(self.tax.c2p(0.5, E), self.tax.c2p(6.5, E), color=AMBER,
                           stroke_width=2.5, dash_length=0.12)
        elab = Text("E = 10 each", font=FONT, font_size=19, color=AMBER).next_to(
            self.tax.c2p(6.5, E), RIGHT, buff=0.1)
        tally_title = Text("tally of 60 rolls", font=FONT, font_size=21, color=TXT).next_to(
            self.tax, UP, buff=0.1)
        self.play(FadeIn(self.tax), FadeIn(face_labels), FadeIn(tally_title), run_time=0.7)
        self.play(Create(eline), FadeIn(elab), run_time=0.6)

        # ---- histogram panel (bottom)
        self.hax = Axes(x_range=[0, 20, 5], y_range=[0, 1, 1],
                        x_length=11.6, y_length=2.05,
                        axis_config=dict(color=GREY, stroke_width=2, include_ticks=True,
                                         include_tip=False),
                        x_axis_config=dict(include_numbers=True, font_size=22,
                                           decimal_number_config={"num_decimal_places": 0,
                                                                  "color": GREY}),
                        y_axis_config=dict(include_ticks=False),
                        ).move_to([0.5, -1.85, 0])
        hxlab = MathTex(r"X^2 = \sum \frac{(O-E)^2}{E}", color=TXT).scale(0.68).move_to(
            self.hax.c2p(18.3, 0.82))
        self.play(FadeIn(self.hax), FadeIn(hxlab), run_time=0.7)

        # ================================================= PART 1: one trial
        self.swap_caption("roll a fair die 60 times — tally the six faces  (every roll real, seeded by today's date)")
        roll_counter = Integer(0, font_size=28, color=BLUE)
        roll_lab = Text("rolls:", font=FONT, font_size=22, color=BLUE)
        roll_row = VGroup(roll_lab, roll_counter).arrange(RIGHT, buff=0.15).move_to([-1.2, 2.3, 0])
        self.play(FadeIn(roll_row), run_time=0.3)

        counts = np.zeros(6, dtype=int)
        bars = self.tally_bars(counts)
        self.add(bars)
        face_show = None
        for k in range(8):                       # first 8 rolls singly, face shown
            f = int(faces[0, k])
            counts[f - 1] += 1
            fs = Text(f"face {f}", font=FONT, font_size=26, color=AMBER).next_to(roll_row, DOWN, buff=0.18)
            anims = [Transform(bars, self.tally_bars(counts)), roll_counter.animate.set_value(k + 1)]
            anims.append(FadeIn(fs) if face_show is None else ReplacementTransform(face_show, fs))
            face_show = fs
            self.play(*anims, run_time=0.32)
        k = 8
        for batch in (12, 20, 20):               # the rest in batches
            for _ in range(batch):
                counts[faces[0, k] - 1] += 1
                k += 1
            anims = [Transform(bars, self.tally_bars(counts)), roll_counter.animate.set_value(k)]
            if face_show is not None:
                anims.append(FadeOut(face_show))
                face_show = None
            self.play(*anims, run_time=0.7)
        assert k == ROLLS and (counts == counts_all[0]).all()

        self.olabels = self.olabels_for(counts)
        self.play(FadeIn(self.olabels), run_time=0.4)
        self.wait(0.4)

        # ---- the table, row by row (upper right)
        self.swap_caption("each face: (O − 10)² / 10 — its miss, in units of its own wobble, squared")
        header = self.row([r"\text{face}", r"O", r"O-10", r"(O-10)^2/10"], HEAD_Y,
                          [TXT, TXT, TXT, PURPLE])
        hline = Line([COL_X[0] - 0.4, LINE_Y, 0], [COL_X[3] + 0.6, LINE_Y, 0],
                     color=GREY, stroke_width=1.2)
        self.play(FadeOut(roll_row), FadeIn(header), Create(hline), run_time=0.5)
        terms, drows = [], []
        for f in range(6):
            o = int(counts[f]); d = o - int(E); term = d * d / E
            terms.append(term)
            r = self.row([str(f + 1), str(o), f"{d:+d}", f"{term:.1f}"], ROW_Y1 - ROW_DY * f,
                         [TXT, BLUE, TXT, PURPLE])
            drows.append(r)
            self.play(FadeIn(r), run_time=0.28)
        x2 = float(X2_all[0])
        assert abs(sum(terms) - x2) < 1e-9
        pieces = [r"X^2 = "]
        for f in range(6):
            pieces.append(f"{terms[f]:.1f}" + (" + " if f < 5 else ""))
        pieces += [r"= ", f"{x2:.1f}"]
        sumrow = MathTex(*pieces, color=TXT).scale(0.62).move_to([2.55, ROW_Y1 - ROW_DY * 6.3, 0])
        for i in range(1, 7):
            sumrow[i].set_color(PURPLE)
        sumrow[-1].set_color(PURPLE)
        self.play(Write(sumrow), run_time=1.0)
        self.wait(0.7)

        # ---- drop the brick
        self.swap_caption(f"add the six:  X² = {x2:.1f} — one honest experiment, one misfit", color=PURPLE)
        UNIT_A = 1 / 8            # stage A: one count = 1/8 of the axis height
        bincounts = np.zeros(N_BINS, dtype=int)
        b = self.bin_of(x2)
        br = self.brick(b, bincounts[b], UNIT_A)
        bincounts[b] += 1
        big = MathTex(f"X^2 = {x2:.1f}", color=PURPLE).scale(0.9).move_to(sumrow.get_center())
        self.play(ReplacementTransform(sumrow, big), run_time=0.4)
        self.play(Transform(big, br), run_time=0.7)
        self.remove(big)
        self.add(br)
        bricks = VGroup(br)
        self.wait(0.6)

        # ================================================= PART 2: many trials
        table_bits = VGroup(header, hline)
        trial_counter = Integer(1, font_size=30, color=BLUE)
        trial_lab = Text("honest dice, 60 rolls each:", font=FONT, font_size=21, color=BLUE)
        trial_row = VGroup(trial_lab, trial_counter).arrange(RIGHT, buff=0.18).move_to([2.55, 2.4, 0])
        self.play(FadeOut(table_bits), FadeOut(VGroup(*drows)), run_time=0.4)
        self.play(FadeIn(trial_row), run_time=0.3)
        self.swap_caption("again — a new die, sixty new rolls, its own X² — and again")

        for t in range(1, 5):                     # trials 2..5 one at a time
            c = counts_all[t]
            x2t = float(X2_all[t])
            num = MathTex(f"X^2 = {x2t:.1f}", color=PURPLE).scale(0.9).move_to([2.55, 1.1, 0])
            self.play(Transform(bars, self.tally_bars(c)), *self.swap_olabels(c),
                      trial_counter.animate.set_value(t + 1), run_time=0.45)
            self.play(FadeIn(num), run_time=0.25)
            b = self.bin_of(x2t)
            br = self.brick(b, bincounts[b], UNIT_A)
            bincounts[b] += 1
            self.play(Transform(num, br), run_time=0.45)
            self.remove(num)
            self.add(br)
            bricks.add(br)

        idx = 5                                   # trials 6..12 in a quick batch, still as bricks
        group = VGroup()
        while idx < 12:
            b = self.bin_of(X2_all[idx])
            group.add(self.brick(b, bincounts[b], UNIT_A))
            bincounts[b] += 1
            idx += 1
        c = counts_all[idx - 1]
        self.play(FadeIn(group, lag_ratio=0.1), Transform(bars, self.tally_bars(c)),
                  *self.swap_olabels(c), trial_counter.animate.set_value(idx), run_time=1.2)
        bricks.add(*group)
        self.wait(0.3)

        # ---- to 100: switch to a normalised scale, in a few jumps
        self.swap_caption("100 honest dice: the pile forms — most misfits sit near 5, the mean of χ² with ν = 5")
        hist = bricks
        for target in (30, 60, 100):
            while idx < target:
                bincounts[self.bin_of(X2_all[idx])] += 1
                idx += 1
            unit = 0.92 / bincounts.max()
            c = counts_all[idx - 1]
            self.play(Transform(hist, self.hist_bars(bincounts, unit)), Transform(bars, self.tally_bars(c)),
                      *self.swap_olabels(c), trial_counter.animate.set_value(idx), run_time=0.9)
        mline = DashedLine(self.hax.c2p(NU, 0), self.hax.c2p(NU, 0.98), color=GREY, stroke_width=2,
                           dash_length=0.1)
        mlab = Text("mean 5 — one unit of miss per free face", font=FONT, font_size=18, color=GREY
                    ).next_to(self.hax.c2p(NU, 0.98), UR, buff=0.06)
        self.play(Create(mline), FadeIn(mlab), run_time=0.6)
        self.wait(1.0)

        # ---- to 1000
        self.swap_caption("1000 honest dice — and the pile smooths into a curve")
        for target in (250, 500, 1000):
            while idx < target:
                bincounts[self.bin_of(X2_all[idx])] += 1
                idx += 1
            unit = 0.92 / bincounts.max()
            c = counts_all[idx - 1]
            self.play(Transform(hist, self.hist_bars(bincounts, unit)), Transform(bars, self.tally_bars(c)),
                      *self.swap_olabels(c), trial_counter.animate.set_value(idx), run_time=0.9)
        assert idx == N_TRIALS
        self.wait(0.4)

        # ---- Pearson's curve, scaled like the bars
        unit = 0.92 / bincounts.max()
        scale = N_TRIALS * BIN_W * unit
        curve = self.hax.plot(lambda x: scale * stats.chi2.pdf(x, NU), x_range=[0.05, 20],
                              color=PURPLE, stroke_width=5)
        clab = MathTex(r"\chi^2_5", color=PURPLE).scale(0.9).move_to(
            self.hax.c2p(7.6, scale * stats.chi2.pdf(5.2, NU)))
        self.swap_caption("Pearson's χ² curve for ν = 5 (1900) — drawn over a pile made of nothing but honest dice",
                          color=PURPLE)
        self.play(Create(curve), FadeIn(clab), run_time=1.6)
        self.wait(1.4)

        # ---- the 5% cut
        beyond = int((X2_all > CRIT).sum())
        cut = Line(self.hax.c2p(CRIT, 0), self.hax.c2p(CRIT, 0.60), color=AMBER, stroke_width=4)
        cutlab = Text(f"5% cut  {CRIT:.2f}", font=FONT, font_size=20, color=AMBER).next_to(
            self.hax.c2p(CRIT, 0.60), UR, buff=0.06)
        self.play(Create(cut), FadeIn(cutlab), run_time=0.6)
        self.wait(0.4)
        beyondlab = Text(f"{beyond} of 1000 honest dice beyond it — {beyond/10:.1f}%",
                         font=FONT, font_size=19, color=AMBER).next_to(cutlab, DOWN, aligned_edge=LEFT, buff=0.12)
        self.play(FadeIn(beyondlab), run_time=0.5)
        self.swap_caption("the table's 5% is honest — and a loaded die's X² will not stay in this pile: that is the test",
                          color=AMBER)
        self.wait(3.2)

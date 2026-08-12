# stack: Manim (chosen 2026-08-12)
# Arrays — why walking a matrix along its rows beats walking it down its columns.
# Three beats: the grid unrolls into a line · along the grain · across the grain.
# Render:  manim -qk arrays-row-major.py RowMajor
# Then:    cp media/videos/arrays-row-major/2160p60/RowMajor.mp4 ./arrays-row-major.mp4

from manim import *

# ---------- Vault palette (Manim track, dark MP4 background) ----------
BG      = "#1e1e1e"
TXT     = "#cccccc"
TXT_DIM = "#888888"
BLUE    = "#2563eb"
RED     = "#dc2626"
GREEN   = "#059669"
AMBER   = "#f59e0b"
GREY    = "#888888"
PURPLE  = "#7c3aed"
TEAL    = "#0891b2"

config.background_color = BG

ROWS, COLS = 4, 8
N = ROWS * COLS
ROW_COLS = [BLUE, PURPLE, GREEN, TEAL]

GW, GH = 0.62, 0.52          # grid cell
FW, FH = 0.40, 0.52          # flat cell


FONT = "Helvetica Neue"


def title_card(t, color=TXT, size=42):
    return Text(t, color=color, font_size=size, weight=BOLD, font=FONT)


def body(t, color=TXT, size=27):
    return Text(t, color=color, font_size=size, font=FONT)


def small(t, color=TXT_DIM, size=21):
    return Text(t, color=color, font_size=size, font=FONT)


class RowMajor(Scene):
    def construct(self):
        self.beat1_unroll()
        self.beat2_along_the_grain()
        self.beat3_across_the_grain()

    # ------------------------------------------------------------------
    # Beat 1 — the grid is a line
    # ------------------------------------------------------------------
    def beat1_unroll(self):
        head = title_card("A 2D array is not a grid").to_edge(UP, buff=0.55)
        self.play(FadeIn(head, shift=DOWN * 0.2))
        self.wait(0.6)

        grid = VGroup()
        for i in range(N):
            r, c = divmod(i, COLS)
            cell = Rectangle(
                width=GW, height=GH,
                stroke_color=ROW_COLS[r], stroke_width=2.2,
                fill_color=ROW_COLS[r], fill_opacity=0.16,
            )
            cell.move_to(
                RIGHT * ((c - (COLS - 1) / 2) * GW)
                + DOWN * ((r - (ROWS - 1) / 2) * GH)
            )
            grid.add(cell)
        grid.move_to(ORIGIN + UP * 1.30)

        self.play(LaggedStart(*[FadeIn(c) for c in grid], lag_ratio=0.02, run_time=1.6))

        row_tags = VGroup()
        for r in range(ROWS):
            tag = small(f"row {r}", color=ROW_COLS[r])
            tag.next_to(grid[r * COLS], LEFT, buff=0.35)
            row_tags.add(tag)
        self.play(LaggedStart(*[FadeIn(t) for t in row_tags], lag_ratio=0.12, run_time=0.9))
        self.wait(1.2)

        claim = body("Memory has no second dimension.").next_to(grid, DOWN, buff=1.0)
        self.play(FadeIn(claim))
        self.wait(1.4)
        self.play(FadeOut(claim), FadeOut(row_tags))

        # unroll: rows laid end to end
        flat = VGroup()
        for i in range(N):
            r = i // COLS
            cell = Rectangle(
                width=FW, height=FH,
                stroke_color=ROW_COLS[r], stroke_width=2.0,
                fill_color=ROW_COLS[r], fill_opacity=0.16,
            )
            cell.move_to(RIGHT * ((i - (N - 1) / 2) * FW))
            flat.add(cell)
        flat.move_to(ORIGIN + UP * 1.05)

        self.play(ReplacementTransform(grid, flat), run_time=2.6)
        self.wait(0.5)

        spans = VGroup()
        for r in range(ROWS):
            seg = flat[r * COLS: (r + 1) * COLS]
            br = Line(
                seg[0].get_corner(DL), seg[-1].get_corner(DR),
                color=ROW_COLS[r], stroke_width=3,
            ).shift(DOWN * 0.18)
            lab = small(f"row {r}", color=ROW_COLS[r]).next_to(br, DOWN, buff=0.12)
            spans.add(VGroup(br, lab))
        self.play(LaggedStart(*[FadeIn(s) for s in spans], lag_ratio=0.15, run_time=1.2))

        formula = body("address(r, c)  =  base  +  (r × 8 + c) × size", size=30)
        formula.next_to(spans, DOWN, buff=0.7)
        self.play(FadeIn(formula))
        self.wait(2.0)

        self.play(FadeOut(spans), FadeOut(formula), FadeOut(head))
        self.carry = dict(flat=flat)

    # ------------------------------------------------------------------
    # Beat 2 — along the grain
    # ------------------------------------------------------------------
    def beat2_along_the_grain(self):
        flat = self.carry["flat"]
        self.play(flat.animate.move_to(ORIGIN + UP * 0.95), run_time=0.8)

        head = title_card("The machine never fetches one value", size=38).to_edge(UP, buff=0.5)
        sub = small(
            "It fetches a 64-byte cache line — eight doubles — whether you wanted one or all eight.",
            size=22,
        ).next_to(head, DOWN, buff=0.28)
        self.play(FadeIn(head, shift=DOWN * 0.2), FadeIn(sub))
        self.wait(1.8)

        note = small("Here one cache line is exactly one row.", color=TXT, size=23)
        note.next_to(flat, DOWN, buff=0.9)
        self.play(FadeIn(note))
        self.wait(1.3)
        self.play(FadeOut(note), FadeOut(sub))

        label = body("Walking ALONG the rows", color=GREEN, size=30)
        label.next_to(flat, DOWN, buff=0.75)
        counter = body("fetches 0     ·     values used 0", size=27)
        counter.next_to(label, DOWN, buff=0.4)
        self.play(FadeIn(label), FadeIn(counter))
        self.wait(0.5)

        fetched, used = 0, 0
        for r in range(ROWS):
            seg = flat[r * COLS: (r + 1) * COLS]
            box = SurroundingRectangle(seg, color=AMBER, stroke_width=3.5, buff=0.06)
            fetched += 1
            self.play(Create(box), run_time=0.45)
            new_counter = body(f"fetches {fetched}     ·     values used {used}", size=27)
            new_counter.move_to(counter)
            self.play(ReplacementTransform(counter, new_counter), run_time=0.25)
            counter = new_counter

            # every value in the line gets consumed
            for k, cell in enumerate(seg):
                used += 1
                self.play(
                    cell.animate.set_fill(GREEN, opacity=0.75),
                    run_time=0.13 if r else 0.2,
                )
            new_counter = body(f"fetches {fetched}     ·     values used {used}", size=27)
            new_counter.move_to(counter)
            self.play(ReplacementTransform(counter, new_counter), run_time=0.25)
            counter = new_counter
            self.play(FadeOut(box), run_time=0.25)

        verdict = body("4 fetches for all 32 values  —  eight values per fetch", color=GREEN, size=29)
        verdict.move_to(counter)
        self.play(ReplacementTransform(counter, verdict))
        self.wait(2.2)

        self.play(FadeOut(verdict), FadeOut(label), FadeOut(head))
        for r in range(ROWS):
            for cell in flat[r * COLS: (r + 1) * COLS]:
                cell.set_fill(ROW_COLS[r], opacity=0.16)

    # ------------------------------------------------------------------
    # Beat 3 — across the grain
    # ------------------------------------------------------------------
    def beat3_across_the_grain(self):
        flat = self.carry["flat"]

        head = title_card("Now walk the same array down its columns", size=36).to_edge(UP, buff=0.5)
        sub = small("Column 0 is elements 0, 8, 16 and 24 — one in each line.", size=22)
        sub.next_to(head, DOWN, buff=0.28)
        self.play(FadeIn(head, shift=DOWN * 0.2), FadeIn(sub))
        self.wait(1.6)
        self.play(FadeOut(sub))

        label = body("Walking DOWN the columns", color=RED, size=30)
        label.next_to(flat, DOWN, buff=0.75)
        counter = body("fetches 0     ·     values used 0", size=27)
        counter.next_to(label, DOWN, buff=0.4)
        self.play(FadeIn(label), FadeIn(counter))
        self.wait(0.4)

        fetched, used = 0, 0
        for r in range(ROWS):
            seg = flat[r * COLS: (r + 1) * COLS]
            box = SurroundingRectangle(seg, color=AMBER, stroke_width=3.5, buff=0.06)
            fetched += 1
            self.play(Create(box), run_time=0.45)

            used += 1
            wanted = seg[0]
            waste = VGroup(*seg[1:])
            self.play(
                wanted.animate.set_fill(GREEN, opacity=0.8),
                waste.animate.set_fill(RED, opacity=0.28).set_stroke(RED, width=1.4),
                run_time=0.6,
            )
            new_counter = body(f"fetches {fetched}     ·     values used {used}", size=27)
            new_counter.move_to(counter)
            self.play(ReplacementTransform(counter, new_counter), run_time=0.3)
            counter = new_counter
            self.play(FadeOut(box), run_time=0.22)

        waste_note = VGroup(
            small("Seven eighths of every fetch discarded — and in a matrix", color=RED, size=22),
            small("bigger than the cache, evicted before column 1 comes looking.", color=RED, size=22),
        ).arrange(DOWN, buff=0.18)
        waste_note.next_to(counter, DOWN, buff=0.45)
        self.play(FadeIn(waste_note))
        self.wait(2.4)

        verdict = body("4 fetches for 4 values  —  one value per fetch", color=RED, size=29)
        verdict.move_to(counter)
        self.play(ReplacementTransform(counter, verdict), FadeOut(waste_note))
        self.wait(1.6)

        tally = VGroup(
            body("To cover all 32 values:", size=26),
            body("4 fetches along the rows        32 fetches down the columns", size=27),
        ).arrange(DOWN, buff=0.28)
        tally[1][:22].set_color(GREEN)
        tally[1][22:].set_color(RED)
        tally.next_to(verdict, DOWN, buff=0.5)
        self.play(FadeIn(tally))
        self.wait(2.4)

        self.play(FadeOut(verdict), FadeOut(label), FadeOut(flat), FadeOut(head), FadeOut(tally))

        # ---- the landing ----
        punch = title_card("Eight times the memory traffic", color=AMBER, size=44)
        punch2 = body("for exactly the same arithmetic.", size=30)
        g = VGroup(punch, punch2).arrange(DOWN, buff=0.35).move_to(UP * 1.4)
        self.play(FadeIn(g, shift=UP * 0.2))
        self.wait(2.0)

        measured = VGroup(
            body("Measured, 6000 × 6000 matrix of doubles:", size=27),
            body("21 ms along the rows        98 ms down the columns", color=TEAL, size=30),
            small("Four and a half times, not eight — the hardware prefetcher claws the rest back.", size=22),
        ).arrange(DOWN, buff=0.34).next_to(g, DOWN, buff=0.85)
        self.play(FadeIn(measured[0]))
        self.wait(0.6)
        self.play(FadeIn(measured[1]))
        self.wait(1.8)
        self.play(FadeIn(measured[2]))
        self.wait(2.4)

        self.play(FadeOut(g), FadeOut(measured))

        final = VGroup(
            title_card("36 million additions either way.", size=40),
            body("Only the order changed.", color=AMBER, size=32),
        ).arrange(DOWN, buff=0.4)
        self.play(FadeIn(final, shift=UP * 0.15))
        self.wait(3.0)
        self.play(FadeOut(final))

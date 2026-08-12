"""
Manim — parallel vs sequential sort race  for  CS/Algorithms/Parallel and External Sorting.md
Renders ONE MP4:  parallel-sort-race.mp4

The "5x either way" story, straight from parallel-sort-benchmark.py on a 10-core Mac
(see parallel-sort-results.json):

  Small job (10,000 items):      1 core 0.014 s   vs   10 cores 0.069 s   ->  parallel 5x SLOWER
  Big   job (10,000,000 items):  1 core 24.9 s    vs   10 cores 4.9 s     ->  parallel 5x FASTER

Each panel races two time-bars. Within a panel the bar lengths AND the draw
run-times are both proportional to the real measured seconds, so the race is
fair; each panel is scaled independently (its slower bar takes ~3 s of screen
time) because the two jobs differ by orders of magnitude. The parallel bar is
split into a GREY overhead segment (spawn workers + split + ship data + merge)
and an AMBER work segment (the actual sort, divided across cores). Overhead
dwarfs the tiny job and nearly vanishes against the huge one — that is the point.

Render (check first):  python3 -m manim -qm parallel-sort-race.py ParallelRace
Render (committed 4K):  manim -qk parallel-sort-race.py ParallelRace
  then copy  media/videos/parallel-sort-race/2160p60/ParallelRace.mp4  ->  ./parallel-sort-race.mp4
  and  rm -rf media  to clear the cache.
"""
from manim import *

# ---- Vault palette (Manim track: fixed dark MP4 background, so text is light) ----
BG   = "#1e1e1e"
TXT  = "#cccccc"
DIM  = "#888888"
BLUE = "#2563eb"
GREEN= "#059669"
AMBER= "#f59e0b"
RED  = "#dc2626"
GREY = "#6b7280"
config.background_color = BG

X0   = -4.3          # left edge of every bar
WMAX = 8.0           # screen width of the longest bar in a panel
BH   = 0.40          # bar height

# real measurements (seconds), 10 cores; oh = the overhead slice of the parallel time
SMALL = dict(n="10,000",     seq=0.0138, par=0.069, oh=0.066,
             verdict="parallel 5× slower", vcol=RED,  oh_label=True)
BIG   = dict(n="10,000,000", seq=24.9,   par=4.9,   oh=1.0,
             verdict="parallel 5× faster", vcol=GREEN, oh_label=False)


class ParallelRace(Scene):
    def construct(self):
        title = VGroup(
            Text("The same 10 cores", color=TXT, weight=BOLD).scale(0.85),
            Text("sorting helps big data, hurts small data", color=DIM).scale(0.5),
        ).arrange(DOWN, buff=0.12).to_edge(UP, buff=0.32)
        self.play(FadeIn(title, shift=DOWN * 0.2))

        self.panel(SMALL, headline_y=2.45)
        self.add(Line([X0 - 1.4, 0.0, 0], [WMAX + X0 + 1.0, 0.0, 0],
                      color=DIM, stroke_width=1).set_opacity(0.3))
        self.panel(BIG, headline_y=-0.65)

        punch = Text("Same 10 cores: 5× slower on the small job, 5× faster on the big one.",
                     color=TXT).scale(0.52).to_edge(DOWN, buff=0.28)
        self.play(Write(punch))
        self.wait(2.5)

    def panel(self, d, headline_y):
        seq_y = headline_y - 0.60
        par_y = headline_y - 1.20
        ver_y = headline_y - 2.05

        wscale = WMAX / max(d["seq"], d["par"])
        seq_w  = d["seq"] * wscale
        oh_w   = d["oh"]  * wscale
        work_w = (d["par"] - d["oh"]) * wscale

        # per-panel time scale so the slower bar draws in ~3 s
        rt = 3.0 / max(d["seq"], d["par"])
        seq_rt, oh_rt, work_rt = d["seq"] * rt, d["oh"] * rt, (d["par"] - d["oh"]) * rt

        head = Text(f"{('Small' if d['oh_label'] else 'Big')} job   ·   {d['n']} items",
                    color=TXT).scale(0.5).move_to([0, headline_y, 0])

        def bar(x_left, w, color, y, op=1.0):
            r = Rectangle(width=max(w, 0.001), height=BH,
                          fill_color=color, fill_opacity=op, stroke_width=0)
            r.move_to([x_left + w / 2, y, 0])
            return r

        seq_bar = bar(X0, seq_w, GREEN, seq_y)
        oh_bar  = bar(X0, oh_w, GREY, par_y, op=0.85)
        work_bar= bar(X0 + oh_w, work_w, AMBER, par_y)

        seq_lab = Text("1 core",   color=DIM).scale(0.42).next_to([X0, seq_y, 0], LEFT, buff=0.25)
        par_lab = Text("10 cores", color=DIM).scale(0.42).next_to([X0, par_y, 0], LEFT, buff=0.25)
        seq_t   = Text(f"{d['seq']:g} s", color=GREEN).scale(0.42)
        par_t   = Text(f"{d['par']:g} s", color=TXT).scale(0.42)

        self.play(FadeIn(head), FadeIn(seq_lab), FadeIn(par_lab), run_time=0.5)
        # the race: both lanes start together; each draws at a speed set by real time
        self.play(
            AnimationGroup(
                GrowFromEdge(seq_bar, LEFT, run_time=seq_rt),
                Succession(GrowFromEdge(oh_bar, LEFT, run_time=oh_rt),
                           GrowFromEdge(work_bar, LEFT, run_time=work_rt)),
                lag_ratio=0.0,
            )
        )
        seq_t.next_to(seq_bar, RIGHT, buff=0.18)
        par_t.next_to(work_bar, RIGHT, buff=0.18)
        self.play(FadeIn(seq_t), FadeIn(par_t), run_time=0.4)

        if d["oh_label"]:
            ohl = Text("fixed overhead: spawn workers · split · ship data · merge",
                       color=DIM).scale(0.33).next_to(oh_bar, DOWN, buff=0.12)
            self.play(FadeIn(ohl), run_time=0.4)

        verdict = Text(d["verdict"], color=d["vcol"], weight=BOLD).scale(0.5).move_to([0, ver_y, 0])
        self.play(FadeIn(verdict, scale=1.1), run_time=0.5)

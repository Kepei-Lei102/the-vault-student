"""
four-colour-manim.py — two scenes for [[Four Colour Theorem]].

Scene 1  PeelAndPaint  — the six-colour proof as a motion: a planar graph is peeled
                         vertex by vertex (always one of degree <= 5), then rebuilt in
                         reverse with each returning vertex taking a free colour.
Scene 2  KempeSwap     — a degree-5 vertex whose neighbours use all five colours;
                         the red–green chain from one neighbour is traced, swapped,
                         and the centre coloured: Heawood's five-colour step.

Smoke:   manim -ql --fps 15 four-colour-manim.py PeelAndPaint KempeSwap
Final:   manim -qk four-colour-manim.py PeelAndPaint KempeSwap
then concat with ffmpeg to four-colour-manim.mp4 and rm -rf media __pycache__.
"""
from manim import *
import numpy as np
import random

GREY = "#888888"
PAL = ["#2563eb", "#dc2626", "#059669", "#f59e0b", "#7c3aed", "#0891b2"]
NAMES = ["blue", "red", "green", "amber", "purple", "teal"]


def planar_graph(seed=7, n=14):
    """A small Delaunay-style planar graph made by hand-ish: random points, edges to near
    neighbours, kept planar by adding edges only when they cross nothing."""
    rng = random.Random(seed)
    pts = []
    while len(pts) < n:
        p = np.array([rng.uniform(-4.2, 4.2), rng.uniform(-1.9, 2.2), 0])
        if all(np.linalg.norm(p - q) > 1.0 for q in pts):
            pts.append(p)
    def cross(a, b, c, d):
        def orient(p, q, r):
            return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
        if len({tuple(a), tuple(b), tuple(c), tuple(d)}) < 4: return False
        return (orient(a, b, c) * orient(a, b, d) < 0) and (orient(c, d, a) * orient(c, d, b) < 0)
    pairs = sorted(((np.linalg.norm(pts[i] - pts[j]), i, j) for i in range(n) for j in range(i + 1, n)))
    edges = []
    for d, i, j in pairs:
        if d > 3.2: break
        if all(not cross(pts[i], pts[j], pts[a], pts[b]) for a, b in edges):
            edges.append((i, j))
    return pts, edges


class PeelAndPaint(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e1e"
        title = Text("Six colours always suffice: peel the map, then paint it back", font_size=30, color=GREY).to_edge(UP, buff=0.3)
        self.play(FadeIn(title))
        pts, edges = planar_graph()
        n = len(pts)
        adj = {i: set() for i in range(n)}
        for a, b in edges:
            adj[a].add(b); adj[b].add(a)
        dots = [Dot(p, radius=0.16, color=GREY) for p in pts]
        labels = [Text(str(len(adj[i])), font_size=16, color="#1e1e1e").move_to(p) for i, p in enumerate(pts)]
        lines = {(a, b): Line(pts[a], pts[b], color=GREY, stroke_width=2.5) for a, b in edges}
        self.play(*[Create(l) for l in lines.values()], run_time=1.0)
        self.play(*[FadeIn(d) for d in dots], *[FadeIn(l) for l in labels], run_time=0.6)
        cap = Text("numbers = how many neighbours; a planar graph always has one with 5 or fewer", font_size=18, color=GREY).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(cap)); self.wait(0.8)

        # peel
        live = {u: set(vs) for u, vs in adj.items()}
        order = []
        while live:
            u = min(live, key=lambda x: (len(live[x]), x))
            order.append(u)
            anims = [dots[u].animate.set_opacity(0.15), labels[u].animate.set_opacity(0)]
            for v in live[u]:
                live[v].discard(u)
                key = (u, v) if (u, v) in lines else (v, u)
                anims.append(lines[key].animate.set_opacity(0.12))
                newl = Text(str(len(live[v])), font_size=16, color="#1e1e1e").move_to(pts[v])
                anims.append(Transform(labels[v], newl))
            del live[u]
            self.play(*anims, run_time=0.35)
        cap2 = Text("now put them back in reverse order — each returns with at most 5 coloured neighbours", font_size=18, color=GREY).to_edge(DOWN, buff=0.35)
        self.play(Transform(cap, cap2)); self.wait(0.5)

        # paint
        col = {}
        for u in reversed(order):
            used = {col[v] for v in adj[u] if v in col}
            c = next(k for k in range(6) if k not in used)
            col[u] = c
            anims = [dots[u].animate.set_opacity(1.0).set_color(PAL[c])]
            for v in adj[u]:
                if v in col:
                    key = (u, v) if (u, v) in lines else (v, u)
                    anims.append(lines[key].animate.set_opacity(1.0))
            self.play(*anims, run_time=0.35)
        used_n = len(set(col.values()))
        cap3 = Text(f"done with {used_n} colour{'s' if used_n > 1 else ''} — never more than six, whatever the map", font_size=20, color=GREY).to_edge(DOWN, buff=0.35)
        self.play(Transform(cap, cap3)); self.wait(1.5)


class KempeSwap(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e1e"
        title = Text("Five colours: the Kempe-chain swap (Heawood, 1890)", font_size=30, color=GREY).to_edge(UP, buff=0.3)
        self.play(FadeIn(title))
        RED, GREEN, BLUE, AMBER, PURPLE = PAL[1], PAL[2], PAL[0], PAL[3], PAL[4]
        v = np.array([0, -0.2, 0])
        th = np.deg2rad(90 + 72 * np.arange(5))
        nb = [v + 1.5 * np.array([np.cos(t), np.sin(t), 0]) for t in th]
        nbcol = [RED, BLUE, GREEN, AMBER, PURPLE]
        chain_pts = [nb[0] + np.array([-0.9, 1.0, 0]), nb[0] + np.array([0.3, 1.5, 0]), nb[0] + np.array([1.6, 1.2, 0])]
        chain_col = [GREEN, RED, GREEN]
        far = nb[2] + np.array([-1.3, -0.6, 0])
        edges = [(v, p) for p in nb] + [(nb[i], nb[(i + 1) % 5]) for i in range(5)] + list(zip([nb[0]] + chain_pts, chain_pts)) + [(nb[2], far)]
        lines = [Line(a, b, color=GREY, stroke_width=2.5) for a, b in edges]
        self.play(*[Create(l) for l in lines], run_time=0.8)
        nbdots = [Dot(p, radius=0.2, color=c) for p, c in zip(nb, nbcol)]
        chdots = [Dot(p, radius=0.17, color=c) for p, c in zip(chain_pts, chain_col)]
        fardot = Dot(far, radius=0.17, color=RED)
        vdot = Dot(v, radius=0.24, color="#1e1e1e", stroke_color=GREY, stroke_width=3)
        self.play(*[FadeIn(d) for d in nbdots + chdots + [fardot, vdot]], run_time=0.6)
        cap = Text("v's five neighbours already use all five colours — nothing is free for v", font_size=19, color=GREY).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(cap)); self.wait(1.0)

        # trace the red-green chain from the red neighbour
        chain_path = [nb[0]] + chain_pts
        glow = [Line(a, b, color=AMBER, stroke_width=10, stroke_opacity=0.35) for a, b in zip(chain_path, chain_path[1:])]
        cap2 = Text("follow red–green from the red neighbour: it never reaches the green neighbour", font_size=19, color=GREY).to_edge(DOWN, buff=0.35)
        self.play(Transform(cap, cap2))
        for g in glow:
            self.play(Create(g), run_time=0.4)
        self.wait(0.6)
        cap3 = Text("swap red and green along that chain only — every border stays two-coloured", font_size=19, color=GREY).to_edge(DOWN, buff=0.35)
        self.play(Transform(cap, cap3))
        self.play(nbdots[0].animate.set_color(GREEN),
                  *[d.animate.set_color(RED if c == GREEN else GREEN) for d, c in zip(chdots, chain_col)], run_time=0.8)
        self.wait(0.5)
        cap4 = Text("no neighbour of v is red any more — paint v red. That is the five-colour theorem's whole engine", font_size=19, color=GREY).to_edge(DOWN, buff=0.35)
        self.play(Transform(cap, cap4))
        self.play(vdot.animate.set_color(RED), FadeOut(VGroup(*glow)), run_time=0.7)
        self.wait(1.8)

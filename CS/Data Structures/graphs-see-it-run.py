# Animation stack: Manim (the bay's standard for its deep cards - Binary Trees,
# Balanced Trees, Hash Tables all carry clips).
# Render:  manim -qk graphs-see-it-run.py GraphsRun
# then copy the MP4 beside the card and delete media/ and __pycache__/.
"""Graphs - the bay's last structure, and the searches that run the world.

Act 1  the constraints dissolve: list, tree, then the graph underneath
Act 2  BFS's ripple vs DFS's dive, same graph, different furniture
Act 3  Dijkstra's empire of certainty on the REAL November 2025 exam graph
"""
from manim import *
import numpy as np

GREY = ManimColor("#888888")
BLUE = ManimColor("#2563eb")
GREEN = ManimColor("#059669")
AMBER = ManimColor("#f59e0b")
RED = ManimColor("#dc2626")
TEAL = ManimColor("#0891b2")


def make_node(label, pos, color=BLUE, r=0.32):
    c = Circle(radius=r, color=color, fill_opacity=0.18, stroke_width=3).move_to(pos)
    t = Text(label, font_size=22, color=GREY).move_to(pos)
    return VGroup(c, t)


class GraphsRun(Scene):
    def construct(self):
        self.act1_dissolve()
        self.act2_ripple_vs_dive()
        self.act3_dijkstra()

    # ------------------------------------------------------------------ Act 1
    def act1_dissolve(self):
        title = Text("every structure in this bay is a graph plus restrictions",
                     font_size=32, color=GREY).to_edge(UP, buff=0.45)
        self.play(FadeIn(title), run_time=1.0)

        labels = list("ABCDEFG")
        list_pos = {l: np.array([-3.9 + i * 1.3, 0.0, 0]) for i, l in enumerate(labels)}
        tree_pos = {"A": np.array([0, 1.7, 0]), "B": np.array([-2.2, 0.35, 0]),
                    "C": np.array([2.2, 0.35, 0]), "D": np.array([-3.2, -1.1, 0]),
                    "E": np.array([-1.1, -1.1, 0]), "F": np.array([1.1, -1.1, 0]),
                    "G": np.array([3.2, -1.1, 0])}
        graph_pos = {"A": np.array([0, 1.8, 0]), "B": np.array([-2.6, 0.8, 0]),
                     "C": np.array([2.6, 0.8, 0]), "D": np.array([-3.1, -1.2, 0]),
                     "E": np.array([-0.5, -0.4, 0]), "F": np.array([1.2, -1.7, 0]),
                     "G": np.array([3.2, -1.3, 0])}

        nodes = {l: make_node(l, list_pos[l]) for l in labels}

        def line_between(a, b, pos, color=GREY, w=3):
            return Line(pos[a], pos[b], color=color, stroke_width=w,
                        buff=0.34)

        list_edges = [line_between(a, b, list_pos) for a, b in zip(labels, labels[1:])]
        caption = Text('the list: "one next each"', font_size=27, color=GREY)
        caption.to_edge(DOWN, buff=0.6)
        self.play(*[FadeIn(nodes[l]) for l in labels],
                  *[Create(e) for e in list_edges], FadeIn(caption), run_time=1.4)
        self.wait(1.0)

        tree_edges_spec = [("A", "B"), ("A", "C"), ("B", "D"), ("B", "E"),
                           ("C", "F"), ("C", "G")]
        new_caption = Text('the tree: "one parent each, no cycles"',
                          font_size=27, color=GREY).to_edge(DOWN, buff=0.6)
        self.play(*[nodes[l].animate.move_to(tree_pos[l]) for l in labels],
                  *[FadeOut(e) for e in list_edges],
                  ReplacementTransform(caption, new_caption), run_time=1.5)
        tree_edges = [line_between(a, b, tree_pos) for a, b in tree_edges_spec]
        self.play(*[Create(e) for e in tree_edges], run_time=1.0)
        caption = new_caption
        self.wait(1.0)

        graph_edges_spec = [("A", "B"), ("A", "C"), ("B", "D"), ("B", "E"),
                            ("A", "E"), ("C", "E"), ("C", "G"), ("E", "F"),
                            ("F", "G"), ("D", "E")]
        cycle = {("A", "B"), ("B", "E"), ("A", "E")}
        new_caption = Text("delete every rule - only connections remain",
                          font_size=27, color=AMBER).to_edge(DOWN, buff=0.6)
        self.play(*[nodes[l].animate.move_to(graph_pos[l]) for l in labels],
                  *[FadeOut(e) for e in tree_edges],
                  ReplacementTransform(caption, new_caption), run_time=1.5)
        graph_edges = [line_between(a, b, graph_pos,
                                    color=AMBER if (a, b) in cycle else GREY,
                                    w=4 if (a, b) in cycle else 3)
                       for a, b in graph_edges_spec]
        self.play(*[Create(e) for e in graph_edges], run_time=1.2)
        cyc_lab = Text("a cycle - finally legal", font_size=25, color=AMBER)
        cyc_lab.move_to(np.array([-4.6, 1.6, 0]))
        self.play(FadeIn(cyc_lab), run_time=0.6)
        self.wait(1.6)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.9)

    # ------------------------------------------------------------------ Act 2
    def act2_ripple_vs_dive(self):
        title = Text("same graph, different furniture", font_size=32, color=GREY)
        title.to_edge(UP, buff=0.4)
        sub = Text("a queue makes a ripple; a stack makes a dive",
                   font_size=26, color=GREY).next_to(title, DOWN, buff=0.2)
        self.play(FadeIn(title), FadeIn(sub), run_time=0.9)

        # a small graph laid out twice
        rel = {"A": np.array([0, 1.35, 0]), "B": np.array([-1.5, 0.45, 0]),
               "C": np.array([1.5, 0.45, 0]), "D": np.array([-1.5, -0.85, 0]),
               "E": np.array([0, -0.2, 0]), "F": np.array([1.5, -0.85, 0]),
               "G": np.array([0, -1.6, 0])}
        edges_spec = [("A", "B"), ("A", "C"), ("B", "D"), ("B", "E"), ("C", "E"),
                      ("C", "F"), ("D", "G"), ("E", "G"), ("F", "G")]
        adj = {v: [] for v in rel}
        for a, b in edges_spec:
            adj[a].append(b)
            adj[b].append(a)

        def build(offset, tint):
            pos = {k: v + offset for k, v in rel.items()}
            nodes = {l: make_node(l, pos[l], color=tint) for l in rel}
            edges = [Line(pos[a], pos[b], color=GREY, stroke_width=2.5, buff=0.32)
                     for a, b in edges_spec]
            return pos, nodes, edges

        posL, nodesL, edgesL = build(np.array([-3.6, -0.6, 0]), TEAL)
        posR, nodesR, edgesR = build(np.array([3.6, -0.6, 0]), BLUE)
        labL = Text("BFS - queue", font_size=27, color=TEAL).move_to([-3.6, 2.0, 0])
        labR = Text("DFS - stack", font_size=27, color=BLUE).move_to([3.6, 2.0, 0])
        self.play(*[FadeIn(m) for m in (*nodesL.values(), *nodesR.values())],
                  *[Create(e) for e in edgesL + edgesR],
                  FadeIn(labL), FadeIn(labR), run_time=1.2)

        # honest orders computed by the card's own algorithms
        from collections import deque
        def bfs(adj, s):
            seen = [s]; q = deque([s])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if v not in seen:
                        seen.append(v); q.append(v)
            return seen
        def dfs(adj, s):
            seen = []; st = [s]
            while st:
                u = st.pop()
                if u not in seen:
                    seen.append(u)
                    st.extend(v for v in adj[u] if v not in seen)
            return seen
        orderL, orderR = bfs(adj, "A"), dfs(adj, "A")

        for i in range(max(len(orderL), len(orderR))):
            anims = []
            if i < len(orderL):
                anims.append(nodesL[orderL[i]][0].animate.set_fill(TEAL, opacity=0.75))
            if i < len(orderR):
                anims.append(nodesR[orderR[i]][0].animate.set_fill(BLUE, opacity=0.75))
            self.play(*anims, run_time=0.55)
        note = Text("one line of code apart: which end of the line you serve first",
                    font_size=26, color=AMBER).to_edge(DOWN, buff=0.45)
        self.play(FadeIn(note), run_time=0.8)
        self.wait(1.6)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.9)

    # ------------------------------------------------------------------ Act 3
    def act3_dijkstra(self):
        title = Text("Dijkstra on the real November 2025 exam graph",
                     font_size=32, color=GREY).to_edge(UP, buff=0.4)
        self.play(FadeIn(title), run_time=0.9)

        pos = {"Start": np.array([-5.6, -1.9, 0]), "T": np.array([-4.6, 0.9, 0]),
               "V": np.array([-1.6, 1.9, 0]), "W": np.array([-0.9, -0.1, 0]),
               "X": np.array([2.2, 0.4, 0]), "Y": np.array([1.6, -2.1, 0]),
               "Z": np.array([5.0, -1.4, 0])}
        Wt = {("Start", "T"): 6, ("Start", "Y"): 22, ("T", "V"): 4, ("V", "W"): 3,
              ("V", "X"): 9, ("W", "X"): 5, ("X", "Y"): 3, ("X", "Z"): 10,
              ("Y", "Z"): 8}
        nodes = {l: make_node(l, pos[l], color=BLUE,
                              r=0.45 if l == "Start" else 0.34) for l in pos}
        edges, wlabels = [], []
        for (a, b), w in Wt.items():
            e = Line(pos[a], pos[b], color=GREY, stroke_width=2.5, buff=0.36)
            edges.append(e)
            mid = (pos[a] + pos[b]) / 2 + np.array([0.0, 0.25, 0])
            wlabels.append(Text(str(w), font_size=22, color=GREY).move_to(mid))
        self.play(*[FadeIn(n) for n in nodes.values()],
                  *[Create(e) for e in edges], *[FadeIn(t) for t in wlabels],
                  run_time=1.3)

        # distance tags, initialised 0 / infinity
        dist_tag = {}
        for l in pos:
            txt = "0" if l == "Start" else "∞"
            tag = Text(txt, font_size=24, color=AMBER)
            tag.next_to(nodes[l], DOWN, buff=0.12)
            dist_tag[l] = tag
        init_note = Text("initialise: Start 0, everyone else ∞",
                         font_size=26, color=AMBER).to_edge(DOWN, buff=0.45)
        self.play(*[FadeIn(t) for t in dist_tag.values()], FadeIn(init_note),
                  run_time=1.0)
        self.wait(0.8)

        # the settle order and updates, exactly as the mark scheme's trace
        steps = [
            ("Start", []),
            ("T", [("V", "10")]),
            ("V", [("W", "13"), ("X", "19")]),
            ("W", [("X", "18")]),
            ("X", [("Y", "21"), ("Z", "28")]),
            ("Y", []),
            ("Z", []),
        ]
        first_updates = {"T": "6", "Y": "22"}   # relaxed when Start settles
        note2 = Text("settle the nearest, relax its neighbours, repeat",
                     font_size=26, color=GREY).to_edge(DOWN, buff=0.45)
        self.play(ReplacementTransform(init_note, note2), run_time=0.7)

        for settle, updates in steps:
            self.play(nodes[settle][0].animate.set_fill(GREEN, opacity=0.7),
                      run_time=0.5)
            ups = dict(updates)
            if settle == "Start":
                ups = first_updates
            anims = []
            for target, newval in ups.items():
                new_tag = Text(newval, font_size=24, color=AMBER)
                new_tag.next_to(nodes[target], DOWN, buff=0.12)
                anims.append(ReplacementTransform(dist_tag[target], new_tag))
                dist_tag[target] = new_tag
            if anims:
                self.play(*anims, run_time=0.6)
        self.wait(0.4)

        # highlight the X improvement story and the Y trap
        trap = Text("the direct Start-Y road of 22 loses by one - keep relaxing",
                    font_size=26, color=RED).to_edge(DOWN, buff=0.45)
        self.play(ReplacementTransform(note2, trap), run_time=0.8)
        self.wait(1.6)
        final = Text("T6  V10  W13  X18  Y21  Z28 - the published answers",
                     font_size=28, color=GREEN).to_edge(DOWN, buff=0.45)
        self.play(ReplacementTransform(trap, final), run_time=0.8)
        self.wait(2.0)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)

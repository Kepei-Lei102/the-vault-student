"""Manim: Balanced Trees — five clips, each paired with the Python that runs it.

Scenes (render each; copy beside the card under the name shown):
  DeletionCases        -> balanced-trees-deletion.mp4
  RotationsAndCases    -> balanced-trees-rotations.mp4
  BalancedTreesSeeItRun-> balanced-trees-see-it-run.mp4   (the plain-vs-AVL race)
  RedBlackRun          -> balanced-trees-redblack.mp4
  BTreeGrow            -> balanced-trees-btree.mp4

All tree logic mirrors balanced-trees-verify.py (the date-seeded harness that
checks every bound); the animations replay the same code the card prints.

Render (from this folder), per scene:
    manim -ql balanced-trees-see-it-run.py DeletionCases          # smoke
    manim -qk balanced-trees-see-it-run.py DeletionCases          # 4K final
Copy media/videos/balanced-trees-see-it-run/2160p60/<Scene>.mp4
  -> the matching kebab-case name beside the card, then rm -rf media/ __pycache__/.
"""

import numpy as np
from manim import (
    Scene, VGroup, VMobject, Text, Circle, Line, Rectangle, RoundedRectangle,
    SurroundingRectangle, FadeIn, FadeOut, Create, Transform, Indicate, Flash,
    UP, DOWN, LEFT, RIGHT, ORIGIN, config,
)

BG = "#1e1e1e"; TXT = "#cccccc"; GREY = "#9a9a9a"
BLUE = "#2563eb"; GREEN = "#059669"; AMBER = "#f59e0b"; RED = "#dc2626"; TEAL = "#0891b2"
FONT = "Helvetica Neue"; MONO = "Menlo"
config.background_color = BG


def caption(s, size=25):
    return Text(s, font=FONT, font_size=size, color=TXT).to_edge(UP, buff=0.3)


def mk_node(v, pos, color=BLUE, r=0.32, fs=20):
    c = Circle(radius=r, color=color, fill_color=color, fill_opacity=0.22,
               stroke_width=3).move_to(pos)
    t = Text(str(v), font=FONT, font_size=fs, color=TXT).move_to(pos)
    return VGroup(c, t)


def mk_edge(p1, p2, r=0.32):
    d = p2 - p1
    u = d / np.linalg.norm(d)
    return Line(p1 + u * r, p2 - u * r, color=GREY, stroke_width=2.2)


class CodePanel(VGroup):
    """Monospace code lines with a movable highlight bar."""
    def __init__(self, lines, x_left=-6.9, y_top=2.6, fs=17, lh=0.42):
        super().__init__()
        self.lines = VGroup()
        for i, ln in enumerate(lines):
            stripped = ln.lstrip(' ')
            ln = '\u00A0' * (len(ln) - len(stripped)) + stripped
            t = Text(ln, font=MONO, font_size=fs, color=TXT)
            t.move_to(np.array([x_left, y_top - i * lh, 0]), aligned_edge=LEFT)
            self.lines.add(t)
        self.add(self.lines)
        self.bar = None

    def highlight(self, scene, i, run_time=0.6):
        new_bar = SurroundingRectangle(self.lines[i], color=AMBER, buff=0.07,
                                       stroke_width=2)
        if self.bar is None:
            self.bar = new_bar
            scene.play(Create(self.bar), run_time=run_time)
        else:
            scene.play(Transform(self.bar, new_bar), run_time=run_time)


# ==================================================================== Deletion
class DeletionCases(Scene):
    def construct(self):
        cap = caption("deletion — three cases, and the code that decides between them")
        code = CodePanel([
            "if root.left is None and \\",
            "   root.right is None:",
            "    return None        # 1: leaf",
            "if root.left is None:",
            "    return root.right  # 2: adopt",
            "if root.right is None:",
            "    return root.left",
            "succ = root.right      # 3: right once,",
            "while succ.left:       #    left to floor",
            "    succ = succ.left",
            "root.data = succ.data",
            "delete(succ) in right subtree",
        ], x_left=-6.9, y_top=2.5, fs=16, lh=0.4)
        self.play(FadeIn(cap), FadeIn(code), run_time=1.1)

        # demo tree 50(30(20,40), 70(60,85)) on the right
        P = {50: np.array([3.6, 2.0, 0]), 30: np.array([2.0, 0.7, 0]),
             70: np.array([5.2, 0.7, 0]), 20: np.array([1.2, -0.7, 0]),
             40: np.array([2.8, -0.7, 0]), 60: np.array([4.4, -0.7, 0]),
             85: np.array([6.0, -0.7, 0])}
        E = {}
        nodes = {}
        for a, b in [(50, 30), (50, 70), (30, 20), (30, 40), (70, 60), (70, 85)]:
            E[(a, b)] = mk_edge(P[a], P[b])
        for v, p in P.items():
            nodes[v] = mk_node(v, p)
        self.play(*[Create(e) for e in E.values()],
                  *[FadeIn(n) for n in nodes.values()], run_time=1.3)
        order = Text("in-order: 20 30 40 50 60 70 85", font=FONT, font_size=21,
                     color=GREY).move_to(np.array([3.6, -2.2, 0]))
        self.play(FadeIn(order), run_time=0.6)
        self.wait(2.0)

        # ---- case 1: delete 20 (leaf)
        cap2 = caption("delete 20 — a leaf: null the parent's pointer, done")
        self.play(Transform(cap, cap2), Indicate(nodes[20], color=RED), run_time=1.0)
        code.highlight(self, 0); code.highlight(self, 2)
        self.play(FadeOut(nodes[20]), FadeOut(E[(30, 20)]), run_time=1.0)
        o2 = Text("in-order: 30 40 50 60 70 85", font=FONT, font_size=21,
                  color=GREY).move_to(order)
        self.play(Transform(order, o2), run_time=0.6)
        self.wait(2.2)

        # ---- case 2: delete 30 (one child, 40)
        cap3 = caption("delete 30 — one child: the parent adopts the grandchild")
        self.play(Transform(cap, cap3), Indicate(nodes[30], color=RED), run_time=1.0)
        code.highlight(self, 3); code.highlight(self, 4)
        new_edge = mk_edge(P[50], P[30])
        self.play(FadeOut(nodes[30]), FadeOut(E[(30, 40)]), run_time=0.8)
        self.play(nodes[40].animate.move_to(P[30]), run_time=1.0)
        self.play(Transform(E[(50, 30)], new_edge), run_time=0.5)
        o3 = Text("in-order: 40 50 60 70 85", font=FONT, font_size=21,
                  color=GREY).move_to(order)
        self.play(Transform(order, o3), run_time=0.6)
        self.wait(2.2)

        # ---- case 3: delete 50 (two children) — successor swap
        cap4 = caption("delete 50 — two children: find the successor (right once, left to the floor)")
        self.play(Transform(cap, cap4), Indicate(nodes[50], color=RED), run_time=1.0)
        code.highlight(self, 7)
        self.play(Indicate(nodes[70], color=AMBER), run_time=0.7)
        code.highlight(self, 8)
        self.play(Indicate(nodes[60], color=AMBER, scale_factor=1.25), run_time=0.9)
        self.wait(0.8)
        cap5 = caption("plant the successor's value in the doomed node — order stays legal")
        self.play(Transform(cap, cap5), run_time=0.7)
        code.highlight(self, 10)
        val60 = Text("60", font=FONT, font_size=20, color=GREEN).move_to(P[60])
        self.add(val60)
        self.play(val60.animate.move_to(P[50]), run_time=1.2)
        self.play(FadeOut(nodes[50][1]), run_time=0.3)
        self.wait(0.7)
        cap6 = caption("then delete the successor below — a leaf: back to the solved case")
        self.play(Transform(cap, cap6), run_time=0.7)
        code.highlight(self, 11)
        self.play(FadeOut(nodes[60]), FadeOut(E[(70, 60)]), run_time=0.9)
        o4 = Text("in-order: 40 60 70 85 — still sorted", font=FONT, font_size=21,
                  color=GREY).move_to(order)
        self.play(Transform(order, o4), run_time=0.6)
        cap7 = caption("the hard case always reduces to an easy one — by construction")
        self.play(Transform(cap, cap7), run_time=0.8)
        self.wait(3.2)


# =================================================================== Rotations
class RotationsAndCases(Scene):
    def construct(self):
        # ---------- Act 1: rot_right, line by line
        cap = caption("the rotation, executed line by line")
        code = CodePanel([
            "def rot_right(y):",
            "    x = y.left",
            "    y.left = x.right   # B moves",
            "    x.right = y        # y swings down",
            "    return x           # x is root now",
        ], x_left=-6.9, y_top=2.2, fs=17, lh=0.46)
        self.play(FadeIn(cap), FadeIn(code), run_time=1.0)

        Py = np.array([3.9, 1.9, 0]); Px = np.array([2.6, 0.6, 0])
        PA = np.array([1.7, -0.9, 0]); PB = np.array([3.4, -0.9, 0]); PC = np.array([5.2, 0.4, 0])
        def tri(p, label):
            t = VMobject(color=TEAL, stroke_width=2.5)
            t.set_points_as_corners([p, p + np.array([-0.5, -0.9, 0]),
                                     p + np.array([0.5, -0.9, 0]), p])
            lab = Text(label, font=FONT, font_size=19, color=GREY).move_to(p + np.array([0, -0.62, 0]))
            return VGroup(t, lab)
        ny, nx = mk_node("y", Py, RED), mk_node("x", Px, RED)
        tA, tB, tC = tri(PA, "A"), tri(PB, "B"), tri(PC, "C")
        e_yx, e_yC = mk_edge(Py, Px), mk_edge(Py, PC, r=0.1)
        e_xA, e_xB = mk_edge(Px, PA, r=0.1), mk_edge(Px, PB, r=0.1)
        self.play(*[FadeIn(m) for m in (ny, nx, tA, tB, tC)],
                  *[Create(e) for e in (e_yx, e_yC, e_xA, e_xB)], run_time=1.2)
        strip = Text("in-order: A x B y C", font=FONT, font_size=21, color=GREY)
        strip.move_to(np.array([3.6, -2.6, 0]))
        self.play(FadeIn(strip), run_time=0.5)
        self.wait(1.8)

        code.highlight(self, 1)
        self.play(Indicate(nx, color=AMBER), run_time=0.8)
        code.highlight(self, 2)
        Qy = np.array([5.0, 0.6, 0]); QB = np.array([4.2, -0.9, 0]); QC = np.array([6.0, -0.9, 0])
        self.play(FadeOut(e_xB), run_time=0.4)
        self.play(tB.animate.move_to(QB + np.array([0, -0.45, 0])), run_time=1.2)
        code.highlight(self, 3)
        Qx = np.array([3.6, 1.9, 0]); QA = np.array([2.4, 0.2, 0])
        self.play(FadeOut(e_yx), FadeOut(e_yC), FadeOut(e_xA), run_time=0.4)
        self.play(ny.animate.move_to(Qy), tC.animate.move_to(QC + np.array([0, -0.45, 0])),
                  nx.animate.move_to(Qx), tA.animate.move_to(QA + np.array([0, -0.45, 0])),
                  run_time=1.6)
        code.highlight(self, 4)
        ne1, ne2 = mk_edge(Qx, Qy), mk_edge(Qx, QA, r=0.1)
        ne3, ne4 = mk_edge(Qy, QB, r=0.1), mk_edge(Qy, QC, r=0.1)
        self.play(*[Create(e) for e in (ne1, ne2, ne3, ne4)], run_time=0.8)
        for n in (nx, ny):
            n[0].set_stroke(GREEN); n[0].set_fill(GREEN, opacity=0.22)
        cap2 = caption("three pointer writes — and the in-order strip never moved")
        self.play(Transform(cap, cap2), Indicate(strip, color=GREEN), run_time=1.0)
        self.wait(2.8)
        self.play(*[FadeOut(m) for m in self.mobjects if m is not cap], run_time=0.7)

        # ---------- Act 2: the four cases, code-paired
        cap3 = caption("four ways to be sick, two moves, one cure")
        code2 = CodePanel([
            "if b > 1 and bal(n.left) >= 0:",
            "    return rot_right(n)        # LL",
            "if b > 1:                      # LR",
            "    n.left = rot_left(n.left)",
            "    return rot_right(n)",
            "if b < -1 and bal(n.right) <= 0:",
            "    return rot_left(n)         # RR",
            "if b < -1:                     # RL",
            "    n.right = rot_right(n.right)",
            "    return rot_left(n)",
        ], x_left=-6.9, y_top=2.4, fs=16, lh=0.4)
        self.play(Transform(cap, cap3), FadeIn(code2), run_time=1.0)

        def show_case(vals, positions, fixed_positions, hl_lines, label, two_step_mid=None, hold=2.0):
            ns = {v: mk_node(v, p, RED, r=0.27, fs=16) for v, p in positions.items()}
            es = []
            ordered = list(positions.items())
            for i in range(len(ordered) - 1):
                es.append(mk_edge(ordered[i][1], ordered[i + 1][1], r=0.27))
            lab = Text(label, font=FONT, font_size=21, color=GREY)
            lab.move_to(np.array([3.7, 2.6, 0]))
            self.play(FadeIn(lab), *[FadeIn(n) for n in ns.values()],
                      *[Create(e) for e in es], run_time=0.9)
            for h in hl_lines[:1]:
                code2.highlight(self, h)
            if two_step_mid is not None:
                # child rotation first: move to intermediate (a straight chain)
                self.wait(0.5)
                code2.highlight(self, hl_lines[1])
                self.play(*[ns[v].animate.move_to(p) for v, p in two_step_mid.items()],
                          *[FadeOut(e) for e in es], run_time=1.3)
                es = []
                mids = list(two_step_mid.items())
                for i in range(len(mids) - 1):
                    e = mk_edge(mids[i][1], mids[i + 1][1], r=0.27)
                    es.append(e)
                self.play(*[Create(e) for e in es], run_time=0.5)
                self.wait(0.6)
                code2.highlight(self, hl_lines[2])
            self.play(*[FadeOut(e) for e in es], run_time=0.3)
            self.play(*[ns[v].animate.move_to(p) for v, p in fixed_positions.items()], run_time=1.2)
            fin = sorted(fixed_positions.items(), key=lambda kv: kv[1][1], reverse=True)
            root = fin[0]
            new_es = [mk_edge(root[1], p, r=0.27) for v, p in fixed_positions.items() if v != root[0]]
            self.play(*[Create(e) for e in new_es], run_time=0.5)
            for v in ns:
                ns[v][0].set_stroke(GREEN); ns[v][0].set_fill(GREEN, opacity=0.22)
            self.wait(hold)
            self.play(FadeOut(lab), *[FadeOut(m) for m in list(ns.values()) + new_es], run_time=0.5)

        FIX = {2: np.array([3.7, 1.4, 0]), 1: np.array([2.6, 0.1, 0]), 3: np.array([4.8, 0.1, 0])}
        show_case([3, 2, 1],
                  {3: np.array([4.6, 1.8, 0]), 2: np.array([3.7, 0.5, 0]), 1: np.array([2.8, -0.8, 0])},
                  FIX, [0], "LL — one right rotation", hold=1.6)
        show_case([1, 2, 3],
                  {1: np.array([2.8, 1.8, 0]), 2: np.array([3.7, 0.5, 0]), 3: np.array([4.6, -0.8, 0])},
                  FIX, [6], "RR — one left rotation", hold=1.6)
        cap4 = caption("LR: the elbow — the child points the wrong way, so straighten it first")
        self.play(Transform(cap, cap4), run_time=0.8)
        show_case([3, 1, 2],
                  {3: np.array([4.6, 1.8, 0]), 1: np.array([2.8, 0.5, 0]), 2: np.array([3.7, -0.8, 0])},
                  FIX, [2, 3, 4], "LR — rotate child LEFT, then rotate RIGHT",
                  two_step_mid={3: np.array([4.6, 1.8, 0]), 2: np.array([3.7, 0.5, 0]), 1: np.array([2.8, -0.8, 0])},
                  hold=2.4)
        show_case([1, 3, 2],
                  {1: np.array([2.8, 1.8, 0]), 3: np.array([4.6, 0.5, 0]), 2: np.array([3.7, -0.8, 0])},
                  FIX, [7, 8, 9], "RL — rotate child RIGHT, then rotate LEFT",
                  two_step_mid={1: np.array([2.8, 1.8, 0]), 2: np.array([3.7, 0.5, 0]), 3: np.array([4.6, -0.8, 0])},
                  hold=2.4)
        cap5 = caption("every case lands on the same balanced triangle — the cure is always a rotation")
        self.play(Transform(cap, cap5), run_time=0.9)
        self.wait(3.0)


# ------------------------------------------------ shared AVL for the race + RB
class _A:
    def __init__(self, v):
        self.v = v; self.l = None; self.r = None; self.h = 1
def _h(n): return n.h if n else 0
def _bal(n): return _h(n.l) - _h(n.r)
def _fix(n): n.h = 1 + max(_h(n.l), _h(n.r))
def _rr(y):
    x = y.l; y.l = x.r; x.r = y; _fix(y); _fix(x); return x
def _rl(x):
    y = x.r; x.r = y.l; y.l = x; _fix(x); _fix(y); return y
def _ains(n, v, events):
    if n is None: return _A(v)
    if v < n.v: n.l = _ains(n.l, v, events)
    else: n.r = _ains(n.r, v, events)
    _fix(n)
    b = _bal(n)
    if b > 1 and _bal(n.l) >= 0:  events.append("LL"); return _rr(n)
    if b > 1:                     events.append("LR"); n.l = _rl(n.l); return _rr(n)
    if b < -1 and _bal(n.r) <= 0: events.append("RR"); return _rl(n)
    if b < -1:                    events.append("RL"); n.r = _rr(n.r); return _rl(n)
    return n
def _height(n):
    return 0 if n is None else 1 + max(_height(n.l), _height(n.r))


class BalancedTreesSeeItRun(Scene):
    """The race, now code-paired: the dispatch line flashes as each rotation fires."""
    CASE_LINE = {"LL": 1, "LR": 2, "RR": 4, "RL": 5}

    def construct(self):
        cap = caption("the race: both trees receive 1, 2, 3, … — the code on watch")
        code = CodePanel([
            "if left-left heavy:",
            "    rot_right(n)          # LL",
            "if left-right:            # LR",
            "    rot_left(child); rot_right(n)",
            "if right-right heavy:",
            "    rot_left(n)           # RR",
            "if right-left:            # RL",
            "    rot_right(child); rot_left(n)",
        ], x_left=-2.1, y_top=-1.5, fs=13, lh=0.30)
        self.play(FadeIn(cap), FadeIn(code), run_time=1.0)
        lab_l = Text("plain BST", font=FONT, font_size=22, color=GREY).move_to(np.array([-4.6, 2.75, 0]))
        lab_r = Text("AVL", font=FONT, font_size=22, color=GREY).move_to(np.array([3.4, 2.75, 0]))
        self.play(FadeIn(lab_l), FadeIn(lab_r), run_time=0.5)

        N = 10
        spine_pos = [np.array([-6.5 + i * 0.32, 2.3 - i * 0.46, 0]) for i in range(N)]
        def layout(root):
            pos, order = {}, []
            def walk(n, d):
                if n is None: return
                walk(n.l, d + 1); order.append((n.v, d)); walk(n.r, d + 1)
            walk(root, 0)
            k = len(order)
            for i, (v, d) in enumerate(order):
                x = 3.4 + (i - (k - 1) / 2) * (4.2 / max(k - 1, 1))
                pos[v] = np.array([x, 2.3 - d * 0.92, 0])
            return pos
        def group(root, pos):
            g = VGroup()
            def walk(n):
                if n is None: return
                if n.l: g.add(mk_edge(pos[n.v], pos[n.l.v], r=0.24))
                if n.r: g.add(mk_edge(pos[n.v], pos[n.r.v], r=0.24))
                walk(n.l); walk(n.r)
            walk(root)
            def walk2(n):
                if n is None: return
                g.add(mk_node(n.v, pos[n.v], GREEN, r=0.24, fs=15))
                walk2(n.l); walk2(n.r)
            walk2(root)
            return g

        hl = Text("height: 0", font=FONT, font_size=20, color=GREY).move_to(np.array([-4.6, -3.3, 0]))
        hr = Text("height: 0", font=FONT, font_size=20, color=GREEN).move_to(np.array([3.4, -3.3, 0]))
        self.play(FadeIn(hl), FadeIn(hr), run_time=0.4)

        root, avl_g = None, None
        for i in range(N):
            v = i + 1
            ln = mk_node(v, spine_pos[i], RED, r=0.2, fs=13)
            adds = [FadeIn(ln)]
            if i > 0:
                adds.append(Create(mk_edge(spine_pos[i - 1], spine_pos[i], r=0.2)))
            events = []
            root = _ains(root, v, events)
            pos = layout(root)
            new_g = group(root, pos)
            if avl_g is None:
                self.play(*adds, FadeIn(new_g), run_time=0.7)
                avl_g = new_g
            else:
                self.play(*adds, Transform(avl_g, new_g), run_time=0.75)
            if events:
                case = events[-1]
                tag = Text(case + "!", font=FONT, font_size=22, color=AMBER)
                tag.move_to(np.array([5.9, 2.6, 0]))
                code.highlight(self, self.CASE_LINE[case], run_time=0.35)
                self.play(FadeIn(tag), run_time=0.3)
                self.play(FadeOut(tag), run_time=0.3)
            nhl = Text(f"height: {i + 1}", font=FONT, font_size=20,
                       color=RED if i > 3 else GREY).move_to(hl)
            nhr = Text(f"height: {_height(root)}", font=FONT, font_size=20, color=GREEN).move_to(hr)
            self.play(Transform(hl, nhl), Transform(hr, nhr), run_time=0.3)
        cap2 = caption("same ten values: the spine reaches 10 — the AVL never leaves 4")
        self.play(Transform(cap, cap2), run_time=0.9)
        self.wait(2.0)
        cap3 = caption("fed 1 to 1023 in order, the AVL lands at height 10 — which is perfect")
        self.play(Transform(cap, cap3), run_time=0.9)
        self.wait(3.6)


# =================================================================== Red-black
class RedBlackRun(Scene):
    def construct(self):
        import math
        RB_RED, RB_BLACK = 0, 1
        class R:
            def __init__(self, v):
                self.v = v; self.l = None; self.r = None; self.p = None; self.c = RB_RED
        class T:
            def __init__(self):
                self.root = None; self.rec = 0; self.rot = 0
            def rl(self, x):
                self.rot += 1
                y = x.r; x.r = y.l
                if y.l: y.l.p = x
                y.p = x.p
                if x.p is None: self.root = y
                elif x is x.p.l: x.p.l = y
                else: x.p.r = y
                y.l = x; x.p = y
            def rr(self, y):
                self.rot += 1
                x = y.l; y.l = x.r
                if x.r: x.r.p = y
                x.p = y.p
                if y.p is None: self.root = x
                elif y is y.p.l: y.p.l = x
                else: y.p.r = x
                x.r = y; y.p = x
            def insert(self, v):
                z = R(v); y, x = None, self.root
                while x is not None:
                    y = x; x = x.l if v < x.v else x.r
                z.p = y
                if y is None: self.root = z
                elif v < y.v: y.l = z
                else: y.r = z
                kinds = []
                while z.p is not None and z.p.c == RB_RED:
                    gp = z.p.p
                    if z.p is gp.l:
                        u = gp.r
                        if u is not None and u.c == RB_RED:
                            z.p.c = RB_BLACK; u.c = RB_BLACK; gp.c = RB_RED
                            self.rec += 1; kinds.append("recolour"); z = gp
                        else:
                            if z is z.p.r: z = z.p; self.rl(z)
                            z.p.c = RB_BLACK; gp.c = RB_RED; self.rr(gp)
                            kinds.append("rotate")
                    else:
                        u = gp.l
                        if u is not None and u.c == RB_RED:
                            z.p.c = RB_BLACK; u.c = RB_BLACK; gp.c = RB_RED
                            self.rec += 1; kinds.append("recolour"); z = gp
                        else:
                            if z is z.p.l: z = z.p; self.rr(z)
                            z.p.c = RB_BLACK; gp.c = RB_RED; self.rl(gp)
                            kinds.append("rotate")
                self.root.c = RB_BLACK
                return kinds

        def rb_node(v, pos, colour):
            if colour == RB_RED:
                c = Circle(radius=0.26, color=RED, fill_color=RED, fill_opacity=0.45,
                           stroke_width=3).move_to(pos)
            else:
                c = Circle(radius=0.26, color=GREY, fill_color="#111111", fill_opacity=1.0,
                           stroke_width=3).move_to(pos)
            t = Text(str(v), font=FONT, font_size=15, color=TXT).move_to(pos)
            return VGroup(c, t)

        def layout(root):
            pos, order = {}, []
            def walk(n, d):
                if n is None: return
                walk(n.l, d + 1); order.append((n.v, d)); walk(n.r, d + 1)
            walk(root, 0)
            k = len(order)
            for i, (v, d) in enumerate(order):
                x = (i - (k - 1) / 2) * (9.5 / max(k - 1, 1))
                pos[v] = np.array([x, 2.1 - d * 0.95, 0])
            return pos

        def group(t):
            pos = layout(t.root)
            g = VGroup()
            def walk(n):
                if n is None: return
                if n.l: g.add(mk_edge(pos[n.v], pos[n.l.v], r=0.26))
                if n.r: g.add(mk_edge(pos[n.v], pos[n.r.v], r=0.26))
                walk(n.l); walk(n.r)
            walk(t.root)
            def walk2(n):
                if n is None: return
                g.add(rb_node(n.v, pos[n.v], n.c))
                walk2(n.l); walk2(n.r)
            walk2(t.root)
            return g

        cap = caption("red-black: feed it sorted 1, 2, 3, … — watch paint do half the work")
        self.play(FadeIn(cap), run_time=0.9)
        counters = Text("recolourings: 0    rotations: 0", font=FONT, font_size=21, color=GREY)
        counters.move_to(np.array([0, -3.3, 0]))
        self.play(FadeIn(counters), run_time=0.5)
        legend = Text("rule: no red parent with a red child · every path, same number of blacks",
                      font=FONT, font_size=18, color=GREY).move_to(np.array([0, -2.75, 0]))
        self.play(FadeIn(legend), run_time=0.6)

        t = T(); g = None
        for v in range(1, 13):
            kinds = t.insert(v)
            new_g = group(t)
            if g is None:
                self.play(FadeIn(new_g), run_time=0.7); g = new_g
            else:
                self.play(Transform(g, new_g), run_time=0.8)
            if kinds:
                word = " + ".join(kinds)
                tag = Text(word, font=FONT, font_size=20,
                           color=AMBER if "rotate" in word else TEAL)
                tag.move_to(np.array([5.4, 2.7, 0]))
                self.play(FadeIn(tag), run_time=0.35)
                self.play(FadeOut(tag), run_time=0.35)
            nc = Text(f"recolourings: {t.rec}    rotations: {t.rot}",
                      font=FONT, font_size=21, color=GREY).move_to(counters)
            self.play(Transform(counters, nc), run_time=0.3)
            if v in (3, 6):
                self.wait(0.8)
        cap2 = caption("the sorted feed cannot build a spine — the rules forbid the shape")
        self.play(Transform(cap, cap2), run_time=0.9)
        self.wait(2.2)
        cap3 = caption("1 to 1023 sorted: height 18 of the allowed 20 — about one rotation per insert")
        self.play(Transform(cap, cap3), run_time=0.9)
        self.wait(3.4)


# ===================================================================== B-tree
class BTreeGrow(Scene):
    ORDER = 4

    def construct(self):
        class N:
            def __init__(self):
                self.keys = []; self.kids = []
        class BT:
            def __init__(self):
                self.root = N()
            def insert(self, k):
                node, path = self.root, []
                while node.kids:
                    path.append(node)
                    i = 0
                    while i < len(node.keys) and k > node.keys[i]: i += 1
                    node = node.kids[i]
                i = 0
                while i < len(node.keys) and k > node.keys[i]: i += 1
                node.keys.insert(i, k)
                grew = False
                while len(node.keys) > BTreeGrow.ORDER - 1:
                    mid = len(node.keys) // 2
                    mk = node.keys[mid]
                    L, Rn = N(), N()
                    L.keys, Rn.keys = node.keys[:mid], node.keys[mid + 1:]
                    if node.kids:
                        L.kids, Rn.kids = node.kids[:mid + 1], node.kids[mid + 1:]
                    if not path:
                        nr = N(); nr.keys = [mk]; nr.kids = [L, Rn]
                        self.root = nr; grew = True
                        break
                    parent = path.pop()
                    j = parent.kids.index(node)
                    parent.kids[j:j + 1] = [L, Rn]
                    parent.keys.insert(j, mk)
                    node = parent
                return grew

        def block(keys, pos, color=GREEN):
            w = max(0.62 * max(len(keys), 1), 0.62)
            r = RoundedRectangle(corner_radius=0.09, width=w, height=0.52,
                                 color=color, fill_color=color, fill_opacity=0.14,
                                 stroke_width=2.4).move_to(pos)
            g = VGroup(r)
            cw = w / max(len(keys), 1)
            for i, k in enumerate(keys):
                g.add(Text(str(k), font=FONT, font_size=16, color=TXT).move_to(
                    pos + np.array([-w / 2 + cw * (i + 0.5), 0, 0])))
            return g

        def layout_group(bt):
            g = VGroup()
            levels = {}
            def collect(n, d):
                levels.setdefault(d, []).append(n)
                for c in n.kids: collect(c, d + 1)
            collect(bt.root, 0)
            pos = {}
            depth = max(levels)
            for d, nodes in levels.items():
                k = len(nodes)
                for i, n in enumerate(nodes):
                    x = (i - (k - 1) / 2) * (11.0 / max(k, 1))
                    pos[id(n)] = np.array([x, 1.9 - d * 1.25, 0])
            def draw(n):
                p = pos[id(n)]
                col = TEAL if n.kids else GREEN
                for c in n.kids:
                    q = pos[id(c)]
                    g.add(Line(p + np.array([0, -0.28, 0]), q + np.array([0, 0.28, 0]),
                               color=GREY, stroke_width=1.8))
                g.add(block(n.keys, p, col))
                for c in n.kids: draw(c)
            draw(bt.root)
            return g

        cap = caption("a B-tree of order 4: full nodes split, the middle key moves UP")
        self.play(FadeIn(cap), run_time=0.9)
        bt = BT(); g = None
        for k in range(1, 11):
            grew = bt.insert(k)
            new_g = layout_group(bt)
            if g is None:
                self.play(FadeIn(new_g), run_time=0.6); g = new_g
            else:
                self.play(Transform(g, new_g), run_time=0.85)
            if grew:
                tag = Text("the ROOT split — the tree grew at the top", font=FONT,
                           font_size=21, color=AMBER).move_to(np.array([0, -2.6, 0]))
                self.play(FadeIn(tag), run_time=0.5)
                self.wait(1.4)
                self.play(FadeOut(tag), run_time=0.4)
            else:
                self.wait(0.25)
        cap2 = caption("no rotations anywhere — and every leaf sits at the same depth, always")
        self.play(Transform(cap, cap2), run_time=0.9)
        self.wait(2.6)
        self.play(FadeOut(g), run_time=0.7)

        # ---- B+ flavour: chained leaves, range scan
        cap3 = caption("the B+ refinement: data only in the leaves — and the leaves are chained")
        self.play(Transform(cap, cap3), run_time=0.9)
        rootP = np.array([0, 1.7, 0])
        leaves_pos = [np.array([-4.4, -0.4, 0]), np.array([0, -0.4, 0]), np.array([4.4, -0.4, 0])]
        rootB = block([31, 62], rootP, TEAL)
        leafB = [block([8, 17, 25], leaves_pos[0]), block([31, 40, 55], leaves_pos[1]),
                 block([62, 74, 88], leaves_pos[2])]
        links = [Line(rootP + np.array([dx, -0.28, 0]), lp + np.array([0, 0.3, 0]),
                      color=GREY, stroke_width=1.8)
                 for dx, lp in zip((-0.62, 0.0, 0.62), leaves_pos)]
        chains = []
        for i in range(2):
            a = leaves_pos[i] + np.array([1.05, 0, 0]); b = leaves_pos[i + 1] + np.array([-1.05, 0, 0])
            chains.append(Line(a, b, color=AMBER, stroke_width=3))
        self.play(FadeIn(rootB), *[FadeIn(l) for l in leafB],
                  *[Create(l) for l in links], run_time=1.1)
        self.play(*[Create(c) for c in chains], run_time=0.9)
        self.wait(1.4)
        cap4 = caption("range query 17…74: descend ONCE, then just walk the chain")
        self.play(Transform(cap, cap4), run_time=0.8)
        walker = Circle(radius=0.34, color=AMBER, stroke_width=3).move_to(rootP)
        self.play(Create(walker), run_time=0.5)
        self.play(walker.animate.move_to(leaves_pos[0] + np.array([0, 0, 0])), run_time=1.0)
        self.play(Indicate(leafB[0], color=AMBER), run_time=0.7)
        self.play(walker.animate.move_to(leaves_pos[1]), run_time=0.9)
        self.play(Indicate(leafB[1], color=AMBER), run_time=0.7)
        self.play(walker.animate.move_to(leaves_pos[2]), run_time=0.9)
        self.play(Indicate(leafB[2], color=AMBER), run_time=0.7)
        cap5 = caption("this is what ORDER BY walks — the index inside MySQL, SQLite, PostgreSQL")
        self.play(Transform(cap, cap5), run_time=0.9)
        self.wait(3.4)

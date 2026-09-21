"""Linked List — the class version, run line by line.

Node objects with a private value and next pointer; the list keeps only Head.
The code panel highlights the line being executed while the drawing does it.

Beat 1: insert(8) into an empty list — Head simply points at the new node.
Beat 2: insert(20) — grip first (NewNode.SetNext(Head)), then move Head.
Beat 3: the two lines swapped — the new node points at itself, the list is lost.
Beat 4: insert(5), insert(13) — each one goes on the front.
Beat 5: remove(20) — Previous and Current walk together; one write unlinks it.
Beat 6: remove(13) — the head has no Previous, so it is a case of its own.
Beat 7: remove(99) — Current walks off the end: return False.

Render:  manim -qk linked-list-class-version.py LinkedListClassVersion
House style: bg #1a1a1a, captions #9a9a9a, teal data, amber pointers,
blue newcomer / Current, purple Previous, red for the mistake.
Deterministic — no randomness.
"""

from manim import *

BG = "#1a1a1a"
GRAYT = "#9a9a9a"
TEAL = "#0891b2"
AMBER = "#f59e0b"
BLUE = "#2563eb"
PURPLE = "#7c3aed"
RED = "#dc2626"
GREEN = "#059669"
MONO = "Menlo"

config.background_color = BG

SLOT_X = [-6.0, -4.15, -2.3, -0.45]
ROW_Y = 0.55
SPAWN = np.array([-6.0, -1.75, 0])
GHOST_Y = -1.85

INSERT_CODE = [
    "def insert(self, Data):",
    "    NewNode = Node(Data)",
    "    if self.__Head is None:",
    "        self.__Head = NewNode",
    "    else:",
    "        NewNode.SetNext(self.__Head)",
    "        self.__Head = NewNode",
]

SWAPPED_CODE = INSERT_CODE[:5] + [INSERT_CODE[6], INSERT_CODE[5]]

REMOVE_CODE = [
    "def remove(self, Data):",
    "    Current = self.__Head",
    "    Previous = None",
    "    if Current is None:",
    "        return False",
    "    if Current.GetValue() == Data:",
    "        self.__Head = self.__Head.GetNext()",
    "        return True",
    "    while Current is not None:",
    "        if Current.GetValue() == Data:",
    "            Previous.SetNext(Current.GetNext())",
    "            return True",
    "        Previous = Current",
    "        Current = Current.GetNext()",
    "    return False",
]


class Box(VGroup):
    """A node: value compartment + next compartment (slash = None)."""

    def __init__(self, value, color=TEAL):
        super().__init__()
        self.value = value
        self.val = Rectangle(width=0.78, height=0.72).set_stroke(GRAYT, 2)
        self.val.set_fill(color, 0.22)
        self.nxt = Rectangle(width=0.5, height=0.72).set_stroke(GRAYT, 2)
        self.nxt.next_to(self.val, RIGHT, buff=0)
        self.txt = Text(str(value), color=color, font_size=28).move_to(self.val)
        self.slash = Line(self.nxt.get_corner(DL) + [0.08, 0.08, 0],
                          self.nxt.get_corner(UR) - [0.08, 0.08, 0],
                          color=GRAYT, stroke_width=2)
        self.add(self.val, self.nxt, self.txt, self.slash)

    def out_point(self):
        return self.nxt.get_center()

    def in_point(self):
        return self.val.get_left()


class LinkedListClassVersion(Scene):
    # ------------------------------------------------------------ helpers
    def caption(self, text, color=GRAYT):
        cap = Text(text, color=color, font_size=23, line_spacing=0.85)
        if cap.width > 7.6:
            cap.scale_to_fit_width(7.6)
        cap.to_edge(LEFT, buff=0.35).set_y(-3.3)
        anims = [FadeIn(cap, run_time=0.3)]
        if getattr(self, "_cap", None) is not None:
            anims.append(FadeOut(self._cap, run_time=0.2))
        self._cap = cap
        self.play(*anims)

    def show_code(self, lines, title):
        group = VGroup()
        for ln in lines:
            indent = (len(ln) - len(ln.lstrip(" "))) // 4
            t = Text(ln.strip(), font=MONO, font_size=15, color="#d4d4d4")
            t.set_x(0, direction=LEFT)
            t.shift(RIGHT * 0.28 * indent)
            group.add(t)
        for i, t in enumerate(group):
            t.set_y(2.95 - i * 0.34)
        group.shift(RIGHT * 0.85)
        head = Text(title, font=MONO, font_size=17, color=GRAYT)
        head.next_to(group, UP, buff=0.22, aligned_edge=LEFT)
        panel = VGroup(head, group)
        old = getattr(self, "_code", None)
        anims = [FadeIn(panel, run_time=0.5)]
        if old is not None:
            anims.append(FadeOut(old, run_time=0.3))
            if self._hl is not None:
                anims.append(FadeOut(self._hl, run_time=0.3))
        self._hl = None
        self._code = panel
        self._lines = group
        self.play(*anims)

    def hl(self, i, wait=0.45):
        line = self._lines[i]
        rect = Rectangle(width=5.9, height=0.3).set_stroke(width=0)
        rect.set_fill(AMBER, 0.22)
        rect.move_to(line).set_x(0.78 + 5.9 / 2)
        if self._hl is None:
            self._hl = rect
            self.play(FadeIn(rect, run_time=0.2))
        else:
            self.play(self._hl.animate.move_to(rect), run_time=0.25)
        if wait:
            self.wait(wait)

    def watch(self, pairs):
        rows = VGroup()
        for name, val, col in pairs:
            rows.add(Text(f"{name} → {val}", font=MONO, font_size=17, color=col))
        rows.arrange(RIGHT, buff=0.55).move_to([4.25, -2.35, 0])
        old = getattr(self, "_watch", None)
        if old is None:
            self.play(FadeIn(rows, run_time=0.25))
        else:
            self.play(FadeOut(old, run_time=0.15), FadeIn(rows, run_time=0.25))
        self._watch = rows

    def arrow(self, a, b, color=AMBER):
        return Arrow(a.out_point(), b.in_point(), buff=0.05, color=color,
                     stroke_width=3.5, max_tip_length_to_length_ratio=0.18)

    def head_arrow(self, node):
        return Arrow(self.head_lbl.get_bottom(), node.val.get_top(), buff=0.08,
                     color=AMBER, stroke_width=3.5,
                     max_tip_length_to_length_ratio=0.18)

    def point(self, a, b, color=AMBER):
        """a.next = b — replace a's slash/arrow with an arrow to b (b None = slash)."""
        anims = []
        old = self.arrows.pop(a, None)
        if old is not None:
            anims.append(FadeOut(old))
        if b is None:
            anims.append(a.slash.animate.set_opacity(1))
            self.nexts[a] = None
        else:
            new = self.arrow(a, b, color)
            self.arrows[a] = new
            self.nexts[a] = b
            anims += [a.slash.animate.set_opacity(0), GrowArrow(new)]
        self.play(*anims, run_time=0.6)

    def set_head(self, node):
        new = self.head_arrow(node) if node is not None else None
        anims = []
        if self.harrow is not None:
            anims.append(FadeOut(self.harrow))
        if new is not None:
            anims.append(GrowArrow(new))
            if self.head_none in self.mobjects:
                anims.append(FadeOut(self.head_none))
        else:
            anims.append(FadeIn(self.head_none))
        self.play(*anims, run_time=0.6)
        self.harrow = new
        self.head = node

    def chain(self):
        out, n = [], self.head
        while n is not None:
            out.append(n)
            n = self.nexts.get(n)
        return out

    def tidy(self, note=True):
        """Redraw the live chain in list order; arrows are rebuilt."""
        order = self.chain()
        fades = [FadeOut(a) for a in self.arrows.values()]
        if self.harrow is not None:
            fades.append(FadeOut(self.harrow))
        self.play(*fades, run_time=0.25)
        self.play(*[n.animate.move_to([SLOT_X[i] + 0.25, ROW_Y, 0])
                    for i, n in enumerate(order)], run_time=0.7)
        self.arrows = {}
        grows = []
        for a, b in zip(order, order[1:]):
            arr = self.arrow(a, b)
            self.arrows[a] = arr
            grows.append(GrowArrow(arr))
        if order:
            self.harrow = self.head_arrow(order[0])
            grows.append(GrowArrow(self.harrow))
        self.play(*grows, run_time=0.4)
        if note:
            self.caption("redrawn in list order — in memory, nothing moved")

    def ghost(self, node, x):
        self.play(node.animate.fade(0.75).move_to([x, GHOST_Y, 0]),
                  *([FadeOut(self.arrows.pop(node))] if node in self.arrows else []),
                  run_time=0.7)
        self.ghosts.append(node)

    def tag(self, name, node, color):
        t = Text(name, font=MONO, font_size=16, color=color)
        pos = node.val.get_bottom() + DOWN * (0.32 if name == "Current" else 0.62)
        t.move_to(pos)
        return t

    def move_tag(self, key, name, node, color):
        old = self.tags.get(key)
        anims = []
        if node is None:
            if old is not None:
                anims.append(FadeOut(old))
            self.tags[key] = None
        else:
            new = self.tag(name, node, color)
            if old is None:
                anims.append(FadeIn(new))
            else:
                anims.append(Transform(old, new))
                new = old
            self.tags[key] = new
        if anims:
            self.play(*anims, run_time=0.35)

    def clear_tags(self):
        fades = [FadeOut(t) for t in self.tags.values() if t is not None]
        if fades:
            self.play(*fades, run_time=0.25)
        self.tags = {}

    # ------------------------------------------------------------ scene
    def construct(self):
        self.arrows, self.nexts, self.tags, self.ghosts = {}, {}, {}, []
        self.head, self.harrow = None, None

        self.head_lbl = Text("Head", font=MONO, font_size=22, color=AMBER)
        self.head_lbl.move_to([SLOT_X[0] - 0.14, 2.35, 0])
        self.head_none = Text("None", font=MONO, font_size=18, color=GRAYT)
        self.head_none.next_to(self.head_lbl, DOWN, buff=0.35)
        title = Text("class LinkedList — the list keeps only Head",
                     font_size=26, color=GRAYT).to_edge(UP, buff=0.3).set_x(-3.3)
        self.play(FadeIn(title), FadeIn(self.head_lbl), FadeIn(self.head_none))
        self.caption("an empty list: Head points nowhere")
        self.wait(0.6)

        # Beat 1 — insert(8)
        self.show_code(INSERT_CODE, "Link.insert(8)")
        self.hl(0)
        self.hl(1, wait=0)
        n8 = Box(8).move_to(SPAWN)
        self.play(FadeIn(n8, shift=UP * 0.2))
        self.caption("Node(8) is made somewhere in memory; its next is None")
        self.hl(2)
        self.hl(3, wait=0)
        self.set_head(n8)
        self.caption("empty list: Head simply points at the new node")
        self.tidy(note=False)
        self.wait(0.5)

        # Beat 2 — insert(20)
        self.show_code(INSERT_CODE, "Link.insert(20)")
        self.hl(1, wait=0)
        n20 = Box(20, BLUE).move_to(SPAWN)
        self.play(FadeIn(n20, shift=UP * 0.2))
        self.hl(2)
        self.hl(4)
        self.hl(5, wait=0)
        self.point(n20, n8)
        self.caption("grip first: the new node points at the old head")
        self.wait(0.8)
        self.hl(6, wait=0)
        self.set_head(n20)
        self.caption("then move Head. Two writes, and 8 never moved")
        self.wait(0.8)
        self.tidy()
        self.play(n20.txt.animate.set_color(TEAL), n20.val.animate.set_fill(TEAL, 0.22))
        self.wait(0.6)

        # Beat 3 — the two lines swapped
        self.show_code(SWAPPED_CODE, "insert(7) — last two lines SWAPPED")
        self._code[0].set_color(RED)
        self.caption("swap the last two lines and run insert(7)…", color=RED)
        self.wait(0.6)
        n7 = Box(7, RED).move_to([-3.4, -1.75, 0])
        self.play(FadeIn(n7, shift=UP * 0.2))
        saved_head = self.harrow
        self.harrow = None
        bad_head = self.head_arrow(n7).set_color(RED)
        self.hl(5, wait=0)
        self.play(FadeOut(saved_head), GrowArrow(bad_head), run_time=0.6)
        self.caption("Head = NewNode first: nobody is holding 20 any more", color=RED)
        self.wait(0.8)
        dimmed = [n20, n8, *self.arrows.values()]
        for m in dimmed:
            m.save_state()
        p0 = n7.nxt.get_center()
        p1 = p0 + RIGHT * 0.6
        p2 = p1 + DOWN * 0.75
        p3 = np.array([n7.val.get_x(), p2[1], 0])
        self.hl(6, wait=0)
        loop = VGroup(
            Line(p0, p1, color=RED, stroke_width=3.5),
            Line(p1, p2, color=RED, stroke_width=3.5),
            Line(p2, p3, color=RED, stroke_width=3.5),
            Arrow(p3, n7.val.get_bottom(), buff=0, color=RED, stroke_width=3.5,
                  max_tip_length_to_length_ratio=0.35),
        )
        self.play(n7.slash.animate.set_opacity(0), Create(loop),
                  *[m.animate.fade(0.7) for m in dimmed],
                  run_time=0.9)
        self.caption("then SetNext(Head): 7 points at itself — 20 and 8 are lost,\n"
                     "and a traversal loops forever", color=RED)
        self.wait(1.6)
        self.play(FadeOut(n7), FadeOut(loop), FadeOut(bad_head),
                  *[Restore(m) for m in dimmed],
                  run_time=0.6)
        self.harrow = self.head_arrow(n20)
        self.play(GrowArrow(self.harrow), run_time=0.4)
        self.caption("undone. The order of those two lines is the whole method")
        self.wait(0.8)

        # Beat 4 — insert(5), insert(13), briskly
        self.caption("two more inserts — the same two writes, in the same order")
        n5, n13 = Box(5, BLUE), Box(13, BLUE)
        for n, label in ((n5, "Link.insert(5)"), (n13, "Link.insert(13)")):
            self.show_code(INSERT_CODE, label)
            n.move_to(SPAWN)
            self.play(FadeIn(n, shift=UP * 0.2), run_time=0.4)
            self.hl(5, wait=0)
            self.point(n, self.head)
            self.hl(6, wait=0)
            self.set_head(n)
            self.tidy(note=False)
            self.play(n.txt.animate.set_color(TEAL),
                      n.val.animate.set_fill(TEAL, 0.22), run_time=0.3)
        self.caption("each insert goes on the front: 13 → 5 → 20 → 8")
        self.wait(1.0)

        # Beat 5 — remove(20)
        self.show_code(REMOVE_CODE, "Link.remove(20)")
        self.hl(0)
        self.hl(1, wait=0)
        self.move_tag("cur", "Current", n13, BLUE)
        self.watch([("Previous", "?", PURPLE), ("Current", "13", BLUE)])
        self.hl(2, wait=0)
        self.watch([("Previous", "None", PURPLE), ("Current", "13", BLUE)])
        self.hl(3)
        self.hl(5)
        self.caption("13 is not 20 — so into the loop")
        self.hl(8)
        self.hl(9)
        self.caption("the loop checks 13 a second time — harmless, one extra comparison")
        self.wait(0.5)
        for prev, cur in ((n13, n5), (n5, n20)):
            self.hl(12, wait=0)
            self.move_tag("prev", "Previous", prev, PURPLE)
            self.watch([("Previous", str(prev.value), PURPLE),
                        ("Current", str(prev.value), BLUE)])
            self.hl(13, wait=0)
            self.move_tag("cur", "Current", cur, BLUE)
            self.watch([("Previous", str(prev.value), PURPLE),
                        ("Current", str(cur.value), BLUE)])
            self.hl(8, wait=0.2)
            self.hl(9)
        self.caption("found: Current is 20, and Previous is right behind it")
        self.wait(0.6)
        self.hl(10, wait=0)
        old = self.arrows.pop(n5)
        skip = CurvedArrow(n5.nxt.get_top(), n8.val.get_top(), angle=-TAU / 5,
                           color=AMBER, stroke_width=3.5)
        self.play(FadeOut(old), Create(skip), run_time=0.8)
        self.nexts[n5] = n8
        self.arrows[n5] = skip
        self.caption("Previous.SetNext(Current.GetNext()): one write, on 5")
        self.wait(0.8)
        self.hl(11, wait=0)
        self.clear_tags()
        self.ghost(n20, -0.2)
        self.caption("20 is unreachable — unlinked, not erased. return True")
        self.wait(0.8)
        self.tidy()
        self.wait(0.4)

        # Beat 6 — remove(13): the head case
        self.show_code(REMOVE_CODE, "Link.remove(13)")
        self.hl(1, wait=0)
        self.move_tag("cur", "Current", n13, BLUE)
        self.watch([("Previous", "None", PURPLE), ("Current", "13", BLUE)])
        self.hl(3)
        self.hl(5)
        self.caption("the head has no Previous — nobody's next to rewrite")
        self.wait(0.8)
        self.hl(6, wait=0)
        self.clear_tags()
        self.set_head(n5)
        self.ghost(n13, -2.1)
        self.caption("so the head is a case of its own: move Head on. return True")
        self.hl(7)
        self.tidy(note=False)
        self.wait(0.4)

        # Beat 7 — remove(99): not found
        self.show_code(REMOVE_CODE, "Link.remove(99)")
        self.hl(1, wait=0)
        self.move_tag("cur", "Current", n5, BLUE)
        self.watch([("Previous", "None", PURPLE), ("Current", "5", BLUE)])
        self.hl(5, wait=0.2)
        self.hl(8, wait=0.2)
        self.hl(9, wait=0.2)
        self.hl(12, wait=0)
        self.move_tag("prev", "Previous", n5, PURPLE)
        self.hl(13, wait=0)
        self.move_tag("cur", "Current", n8, BLUE)
        self.watch([("Previous", "5", PURPLE), ("Current", "8", BLUE)])
        self.hl(8, wait=0.2)
        self.hl(9, wait=0.2)
        self.hl(12, wait=0)
        self.move_tag("prev", "Previous", n8, PURPLE)
        self.watch([("Previous", "8", PURPLE), ("Current", "8", BLUE)])
        self.hl(13, wait=0)
        self.move_tag("cur", "Current", None, BLUE)
        self.watch([("Previous", "8", PURPLE), ("Current", "None", BLUE)])
        self.caption("Current walks off the end, onto None")
        self.hl(8)
        self.hl(14)
        self.caption("the loop ends without a match: return False")
        self.wait(0.8)
        self.clear_tags()

        # End card
        summary = Text("insert: two writes at the head — grip first, then move Head\n"
                       "remove: walk Previous and Current together — one write\n"
                       "the head is special: it has no Previous",
                       font_size=22, color=GREEN, line_spacing=0.9)
        summary.to_edge(LEFT, buff=0.35).set_y(-3.15)
        self.play(FadeOut(self._cap), FadeIn(summary))
        self._cap = summary
        self.wait(2.5)

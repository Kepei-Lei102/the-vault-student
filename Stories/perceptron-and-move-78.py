"""
perceptron-and-move-78.py — the two lineages, each run once.

Companion to [[Stories/The Perceptron and Move 78]].

  1. ROSENBLATT'S PERCEPTRON (1958) with his learning rule — the statistical lineage's
     first machine.  Trained on AND, OR and XOR: it learns the first two in a handful of
     passes and never learns the third, however long it runs — Minsky and Papert's 1969
     theorem, reproduced.  Then one hidden layer, and XOR falls (the fix everyone knew and
     nobody could train until back propagation).
  2. MONTE CARLO TREE SEARCH (2006) — the symbolic lineage's last great trick before the
     marriage: a player for noughts and crosses that knows no strategy, only the rules, and
     plays out random games to judge moves.  Against a random opponent it loses almost never,
     and the more play-outs it is given, the closer 'almost' gets to 'never'.

Run:  python3 perceptron-and-move-78.py
"""
import math, random
import numpy as np

# ------------------------------------------------------------- 1. the perceptron
def perceptron(X, y, epochs=200, lr=0.1):
    w = np.zeros(X.shape[1]); b = 0.0
    for ep in range(1, epochs + 1):
        errors = 0
        for xi, yi in zip(X, y):
            out = 1 if xi @ w + b > 0 else 0
            if out != yi:
                w += lr * (yi - out) * xi; b += lr * (yi - out); errors += 1   # Rosenblatt's rule: nudge toward the miss
        if errors == 0: return ep, w, b
    return None, w, b

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], float)
print("1. Rosenblatt's perceptron, one unit, learning rule of 1958:")
for name, y in (("AND", [0, 0, 0, 1]), ("OR", [0, 1, 1, 1]), ("XOR", [0, 1, 1, 0])):
    ep, w, b = perceptron(X, np.array(y), epochs=1000)
    print(f"   {name}: " + (f"learned in {ep} passes — line {w[0]:+.1f}x + {w[1]:+.1f}y {b:+.1f} = 0 separates them" if ep else "never learned in 1000 passes — no straight line separates (0,1),(1,0) from (0,0),(1,1)"))
# one hidden layer, trained by back propagation (the 1986 fix)
rng = np.random.default_rng(1969)
W1 = rng.normal(0, 1, (2, 3)); b1 = np.zeros(3); W2 = rng.normal(0, 1, 3); b2 = 0.0
y = np.array([0, 1, 1, 0], float); sig = lambda z: 1 / (1 + np.exp(-z))
for ep in range(5000):
    h = sig(X @ W1 + b1); out = sig(h @ W2 + b2)
    d2 = (out - y) * out * (1 - out); d1 = np.outer(d2, W2) * h * (1 - h)
    W2 -= 0.5 * h.T @ d2; b2 -= 0.5 * d2.sum(); W1 -= 0.5 * X.T @ d1; b1 -= 0.5 * d1.sum(0)
print(f"   XOR with three hidden units and back propagation: outputs {np.round(sig(sig(X @ W1 + b1) @ W2 + b2), 2)} — solved; Minsky knew the layer would do it, and nobody knew how to train it until 1986")

# ------------------------------------------------------------- 2. Monte Carlo tree search
LINES = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
def winner(b):
    for a, c, d in LINES:
        if b[a] and b[a] == b[c] == b[d]: return b[a]
    return 0 if 0 in b else 2   # 2 = draw
def moves(b): return [i for i in range(9) if b[i] == 0]

class Node:
    def __init__(self, board, player, parent=None, move=None):
        self.board, self.player, self.parent, self.move = board, player, parent, move
        self.children = []; self.n = 0; self.w = 0.0
        self.untried = moves(board) if winner(board) == 0 else []      # a finished game has no moves left
    def uct(self, c=1.4):
        return max(self.children, key=lambda ch: ch.w / ch.n + c * math.sqrt(math.log(self.n) / ch.n))

def mcts(board, player, iters=400):
    root = Node(board, player)
    for _ in range(iters):
        node = root
        while not node.untried and node.children: node = node.uct()                 # select
        if node.untried:                                                             # expand
            m = node.untried.pop(random.randrange(len(node.untried)))
            nb = node.board[:]; nb[m] = node.player
            child = Node(nb, -node.player, node, m); node.children.append(child); node = child
        b = node.board[:]; p = node.player; res = winner(b)                          # simulate: random play-out
        while res == 0:
            m = random.choice(moves(b)); b[m] = p; p = -p; res = winner(b)
        while node:                                                                  # back up
            node.n += 1
            if res == 2: node.w += 0.5
            elif res == -node.player: node.w += 1     # the player who moved INTO this node won
            node = node.parent
    return max(root.children, key=lambda ch: ch.n).move

def play(mcts_first, iters=400):
    b = [0] * 9; p = 1
    while winner(b) == 0:
        m = mcts(b, p, iters) if (p == 1) == mcts_first else random.choice(moves(b))
        b[m] = p; p = -p
    r = winner(b)
    return "draw" if r == 2 else ("mcts" if (r == 1) == mcts_first else "random")

random.seed(2006)
print("\n2. Monte Carlo tree search — noughts and crosses, no strategy programmed, only the rules and random play-outs:")
for iters in (100, 400, 2000):
    for first in (True, False):
        tally = {"mcts": 0, "draw": 0, "random": 0}
        for _ in range(100): tally[play(first, iters)] += 1
        print(f"   {iters:4d} play-outs per move, MCTS {'first ' if first else 'second'} vs random, 100 games: wins {tally['mcts']:3d}, draws {tally['draw']:2d}, losses {tally['random']}")
print("   — judging a position by playing it out at random, thousands of times, was the search half of AlphaGo; the network supplied the judgement instead of the dice")

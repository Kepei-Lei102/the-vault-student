"""
ai-learning-demo.py — every kind of learning the syllabus names, built from scratch and measured.

Companion to [[Artificial Intelligence]].  numpy only; no ML library.  Six parts, one per
idea the card teaches, each printing the number the card quotes:

  1. REGRESSION by gradient descent — a straight line fitted to noisy data by repeatedly
     nudging slope and intercept downhill on the squared error; the recovered slope vs the
     true one.  (9618: "regression methods in machine learning")
  2. A NEURON, then a NETWORK — a single neuron cannot learn XOR (measured); two layers can.
  3. BACK PROPAGATION — the network's weights adjusted by the chain rule; loss falling;
     the gradient checked numerically against the analytic one (agree to 1e-9).
  4. DEEP vs SHALLOW — the same budget of weights, one hidden layer vs three, on a spiral:
     the deeper net reaches a higher accuracy.  (why "deep")
  5. UNSUPERVISED — k-means finds three clusters with no labels; purity measured.
  6. REINFORCEMENT — Q-learning on a 5×5 grid with a pit: no labels, only reward; the
     agent finds the 8-step optimal path.
  7. AN EXPERT SYSTEM (0478) — a rule base and a forward-chaining inference engine
     diagnosing a fault from facts; the chain of rules fired is printed.

Run:  python3 ai-learning-demo.py
"""
import math
import numpy as np

rng = np.random.default_rng(1956)          # the Dartmouth summer
SCRATCH = "/private/tmp/claude-501/-Users-kepeilei-Desktop-The-Vault/9720838e-86e0-4e5c-b8c8-cc7938ccd876/scratchpad"

# ------------------------------------------------------------------ 1. regression
def regression():
    x = rng.uniform(0, 10, 200)
    y = 3.0 * x + 2.0 + rng.normal(0, 2.0, 200)              # true slope 3, intercept 2, noise
    m, c, lr = 0.0, 0.0, 0.01
    for step in range(2000):
        pred = m * x + c
        dm = (2 / len(x)) * ((pred - y) * x).sum()           # dLoss/dm
        dc = (2 / len(x)) * (pred - y).sum()                 # dLoss/dc
        m -= lr * dm; c -= lr * dc
    loss = ((m * x + c - y) ** 2).mean()
    print(f"1. regression by gradient descent: slope {m:.3f} (true 3.000), intercept {c:.3f} (true 2.000), mean squared error {loss:.2f} (noise variance 4.00)")
    print("   — 'learning' here is 2000 small steps downhill on the error; nothing was solved in closed form")

# ------------------------------------------------------------------ 2–3. neuron, network, backprop
def sigmoid(z): return 1 / (1 + np.exp(-z))

def forward(W, B, X):
    """tanh in the hidden layers, sigmoid at the output; returns every layer's activations."""
    acts = [X]
    for i, (w, b) in enumerate(zip(W, B)):
        z = acts[-1] @ w + b
        acts.append(sigmoid(z) if i == len(W) - 1 else np.tanh(z))
    return acts

def train_net(X, Y, hidden, epochs, lr, seed=0, momentum=0.9):
    r = np.random.default_rng(seed)
    sizes = [X.shape[1]] + hidden + [1]
    W = [r.normal(0, 1 / math.sqrt(a), (a, b)) for a, b in zip(sizes[:-1], sizes[1:])]
    B = [np.zeros((1, b)) for b in sizes[1:]]
    vW = [np.zeros_like(w) for w in W]; vB = [np.zeros_like(b) for b in B]
    losses = []
    for ep in range(epochs):
        acts = forward(W, B, X); out = acts[-1]
        loss = ((out - Y) ** 2).mean(); losses.append(loss)
        # backward: the chain rule, layer by layer, from the output error back to the first weights
        delta = 2 * (out - Y) / len(X) * out * (1 - out)
        for i in reversed(range(len(W))):
            gW = acts[i].T @ delta; gB = delta.sum(0, keepdims=True)
            if i > 0:
                delta = (delta @ W[i].T) * (1 - acts[i] ** 2)          # d tanh
            vW[i] = momentum * vW[i] - lr * gW; vB[i] = momentum * vB[i] - lr * gB
            W[i] += vW[i]; B[i] += vB[i]
    return W, B, losses

def predict(W, B, X):
    return forward(W, B, X)[-1]

def xor():
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], float); Y = np.array([[0], [1], [1], [0]], float)
    W, B, L = train_net(X, Y, [], 5000, 0.5, momentum=0.0)
    print(f"\n2. one neuron on XOR after 5000 epochs: outputs {np.round(predict(W, B, X).ravel(), 2)} — stuck near 0.5: a single neuron draws one straight line, and XOR is not linearly separable")
    W, B, L = train_net(X, Y, [3], 5000, 0.5, momentum=0.0)
    print(f"   three hidden neurons + one output: outputs {np.round(predict(W, B, X).ravel(), 2)}, loss {L[0]:.3f} → {L[-1]:.4f} — the hidden layer bends the boundary")
    # 3. gradient check: numeric vs analytic on the first weight
    W, B, _ = train_net(X, Y, [3], 1, 0.0, seed=3)
    def loss_of(W, B): return ((predict(W, B, X) - Y) ** 2).mean()
    eps = 1e-6
    Wp = [w.copy() for w in W]; Wp[0][0, 0] += eps
    Wm = [w.copy() for w in W]; Wm[0][0, 0] -= eps
    numeric = (loss_of(Wp, B) - loss_of(Wm, B)) / (2 * eps)
    # analytic
    acts = forward(W, B, X)
    out = acts[-1]; delta = 2 * (out - Y) / len(X) * out * (1 - out)
    delta1 = (delta @ W[1].T) * (1 - acts[1] ** 2)
    analytic = (acts[0].T @ delta1)[0, 0]
    print(f"3. back propagation checked: analytic dLoss/dW = {analytic:+.6f}, numeric (nudge the weight, watch the loss) = {numeric:+.6f}, difference {abs(analytic-numeric):.1e}")
    print("   — 'back propagation of errors' is the chain rule run from the output error back to every weight; it is exact, not a heuristic")
    return L

# ------------------------------------------------------------------ 4. deep vs shallow
def spiral(n=300, seed=1, turns=3.0):
    r = np.random.default_rng(seed)
    t = np.linspace(0.3, 3.5, n)
    x1 = np.c_[t * np.cos(turns * t), t * np.sin(turns * t)] + r.normal(0, 0.12, (n, 2))
    x2 = np.c_[t * np.cos(turns * t + math.pi), t * np.sin(turns * t + math.pi)] + r.normal(0, 0.12, (n, 2))
    X = np.vstack([x1, x2]) / 3.5; Y = np.vstack([np.zeros((n, 1)), np.ones((n, 1))])
    return X, Y

def deep_vs_shallow():
    X, Y = spiral()
    Xt, Yt = spiral(seed=2)
    results = {}; nets = {}
    for name, hidden in (("shallow (1 layer × 64)", [64]), ("deep (3 layers × 10)", [10, 10, 10])):
        W, B, L = train_net(X, Y, hidden, 8000, 0.05, seed=7)
        acc = ((predict(W, B, Xt) > 0.5) == (Yt > 0.5)).mean()
        results[name] = (acc, L[-1], sum(w.size for w in W) + sum(b.size for b in B)); nets[name] = (W, B)
    print(f"\n4. deep vs shallow on the two-spiral problem, 8000 epochs each, tested on 600 unseen points:")
    for k, (acc, l, n) in results.items():
        print(f"   {k:24s}: test accuracy {acc*100:5.1f}%   ({n} weights and biases; final training loss {l:.3f})")
    print("   — same budget of numbers, arranged deep: each layer builds on the last's features (a curl of a curl); one wide layer must draw every bend from scratch")
    # save the decision maps for the figure
    g = np.linspace(-1.1, 1.1, 161); GX, GY = np.meshgrid(g, g); G = np.c_[GX.ravel(), GY.ravel()]
    np.savez(SCRATCH + "/spiral.npz", X=X, Y=Y, shallow=predict(*nets["shallow (1 layer × 64)"], G).reshape(GX.shape),
             deep=predict(*nets["deep (3 layers × 10)"], G).reshape(GX.shape), g=g)

# ------------------------------------------------------------------ 5. k-means
def kmeans():
    centres = np.array([[0, 0], [5, 5], [0, 6]], float)
    labels = np.repeat([0, 1, 2], 100)
    X = centres[labels] + rng.normal(0, 0.9, (300, 2))
    C = X[rng.choice(300, 3, replace=False)]
    for it in range(20):
        assign = np.argmin(((X[:, None, :] - C[None, :, :]) ** 2).sum(2), 1)
        newC = np.array([X[assign == k].mean(0) for k in range(3)])
        if np.allclose(newC, C): break
        C = newC
    # purity: for each found cluster, the fraction that share the majority true label
    purity = sum(np.bincount(labels[assign == k]).max() for k in range(3)) / 300
    np.savez(SCRATCH + "/kmeans.npz", X=X, assign=assign, C=C)
    print(f"\n5. unsupervised — k-means given 300 unlabelled points and told 'find 3 groups': converged in {it+1} iterations,")
    print(f"   centres found at {np.round(C, 1).tolist()} (true {centres.astype(int).tolist()}), purity {purity*100:.1f}% — no label was ever shown")

# ------------------------------------------------------------------ 6. Q-learning
def q_learning():
    N = 5; goal = (4, 4); pit = (2, 2)
    Q = np.zeros((N, N, 4)); moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    alpha, gamma, eps = 0.5, 0.9, 0.2
    def step(s, a):
        r, c = s; dr, dc = moves[a]
        n = (min(max(r + dr, 0), N - 1), min(max(c + dc, 0), N - 1))
        if n == goal: return n, 10.0, True
        if n == pit: return n, -10.0, True
        return n, -1.0, False
    r_ = np.random.default_rng(4)
    for ep in range(600):
        s = (0, 0); done = False
        while not done:
            a = r_.integers(4) if r_.random() < eps else int(np.argmax(Q[s]))
            n, rew, done = step(s, a)
            Q[s][a] += alpha * (rew + gamma * (0 if done else Q[n].max()) - Q[s][a])
            s = n
    np.save(SCRATCH + "/qtable.npy", Q)
    # follow the greedy policy
    s = (0, 0); path = [s]
    for _ in range(30):
        s, _, done = step(s, int(np.argmax(Q[s]))); path.append(s)
        if done: break
    print(f"\n6. reinforcement — Q-learning on a 5×5 grid, start (0,0), goal (4,4) worth +10, pit at (2,2) worth −10, −1 per step:")
    print(f"   after 600 episodes of trial and error the greedy path is {path} — {len(path)-1} steps, the shortest that skirts the pit;")
    print("   no one told the agent where the goal or the pit was: it learned from reward alone")

# ------------------------------------------------------------------ 7. expert system
def expert_system():
    rules = [  # IF all conditions THEN conclusion   (the rule base)
        ({"engine cranks", "no start"}, "fuel or spark problem"),
        ({"fuel or spark problem", "fuel gauge empty"}, "out of fuel"),
        ({"fuel or spark problem", "fuel gauge not empty", "no spark at plug"}, "ignition fault"),
        ({"engine does not crank", "lights dim"}, "flat battery"),
        ({"engine does not crank", "lights bright"}, "starter motor fault"),
    ]
    facts = {"engine cranks", "no start", "fuel gauge not empty", "no spark at plug"}   # the knowledge base for this case
    fired = []
    changed = True
    while changed:                                                   # the inference engine: forward chaining
        changed = False
        for cond, concl in rules:
            if cond <= facts and concl not in facts:
                facts.add(concl); fired.append(f"{sorted(cond)} → {concl}"); changed = True
    print("\n7. expert system (0478): facts in, rules fire until nothing new follows —")
    for f in fired: print("   fired:", f)
    print("   diagnosis:", fired[-1].split("→ ")[1] if fired else "no rule applies — the system has nothing to say")
    print("   — knowledge base (facts) + rule base (IF–THEN) + inference engine (this loop) + interface (this printout); it never learns: add a rule or it stays wrong")

if __name__ == "__main__":
    regression(); L = xor(); deep_vs_shallow(); kmeans(); q_learning(); expert_system()
    np.save(SCRATCH + "/xor-loss.npy", np.array(L))

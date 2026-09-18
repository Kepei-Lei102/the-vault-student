"""
rl-environment-sim.py — three things a reinforcement learner cannot out-learn, measured.

Companion to [[You Are a Reinforcement Learner]].  Plain Q-learning (the same update as
[[Artificial Intelligence]]'s gridworld), run inside environments that differ only in their
reward signal.  The agent is identical every time; only the environment changes.

  1. A PROPER REWARD vs A PROXY — the goal is to deliver a parcel across a grid; a
     "broken" environment pays per checkpoint tag instead of per delivery.  The same
     agent learns to deliver in the first and to circle the checkpoints forever in the
     second: reward hacking, Goodhart's law in twenty lines.
  2. DELAY — the same delivery task, reward paid at once vs paid k steps late (the
     institution that notices in three years).  Episodes to learn, as a function of delay.
  3. EXTINCTION — a "helper" agent chooses each round whether to help a neighbour at a
     small cost.  When the neighbour rewards help (thanks, credit, pay), helping is
     learned and kept; when the neighbour never does, helping is learned *and then
     unlearned*.  The rate of helping over time in both worlds.

Run:  python3 rl-environment-sim.py
"""
import numpy as np

SCRATCH = "/private/tmp/claude-501/-Users-kepeilei-Desktop-The-Vault/9720838e-86e0-4e5c-b8c8-cc7938ccd876/scratchpad"
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def q_run(step_fn, n_states, episodes, alpha=0.5, gamma=0.9, eps=0.15, seed=0, max_steps=200):
    rng = np.random.default_rng(seed)
    Q = np.zeros((n_states, 4)); history = []
    for ep in range(episodes):
        s = 0; done = False; total = 0.0; goal_hit = False; tags = 0
        for t in range(max_steps):
            a = rng.integers(4) if rng.random() < eps else int(np.argmax(Q[s]))
            n, r, done, info = step_fn(s, a, t)
            Q[s, a] += alpha * (r + gamma * (0 if done else Q[n].max()) - Q[s, a])
            total += r; s = n; goal_hit = goal_hit or info.get("delivered", False); tags += info.get("tag", 0)
            if done: break
        history.append((total, goal_hit, tags, t + 1))
    return Q, history

# ------------------------------------------------------------ 1. proper reward vs proxy
N = 6
def to_s(r, c): return r * N + c
def move(s, a):
    r, c = divmod(s, N); dr, dc = MOVES[a]
    return to_s(min(max(r + dr, 0), N - 1), min(max(c + dc, 0), N - 1))
GOAL = to_s(5, 5); CHECKPOINTS = {to_s(1, 3), to_s(3, 1)}

def proper(s, a, t):
    n = move(s, a)
    if n == GOAL: return n, 10.0, True, {"delivered": True}
    return n, -0.1, False, {}

def proxy(s, a, t):            # the institution pays per checkpoint tag, "because deliveries are hard to measure"
    n = move(s, a)
    if n == GOAL: return n, 10.0, True, {"delivered": True}
    if n in CHECKPOINTS: return n, 1.0, False, {"tag": 1}
    return n, -0.1, False, {}

def part1():
    print("1. the same agent, two reward signals (6×6 grid, parcel at the far corner, 400 episodes each):")
    for name, fn in (("proper: paid on delivery", proper), ("proxy: paid per checkpoint tag", proxy)):
        Q, H = q_run(fn, N * N, 400, seed=1)
        np.save(SCRATCH + f"/part1-{'proper' if fn is proper else 'proxy'}.npy", np.array([[h[1], h[2]] for h in H], float))
        last = H[-50:]
        print(f"   {name:32s} last 50 episodes — delivered {100*np.mean([h[1] for h in last]):5.1f}% of the time, "
              f"{np.mean([h[2] for h in last]):5.1f} checkpoint tags per episode, {np.mean([h[3] for h in last]):5.1f} steps")
    print("   — the proxy agent is not stupid and not lazy: it has learned exactly what it was paid for")
    return

# ------------------------------------------------------------ 2. delay
def part2():
    print("\n2. delay — the delivery reward paid k steps late; the agent keeps acting meanwhile (60-step episodes, 1500 of them):")
    rows = []
    for k in (0, 1, 3, 6, 12):
        rng = np.random.default_rng(2); Q = np.zeros((N * N, 4)); steps_to = []
        for ep in range(1500):
            s = 0; pending = []; first = None
            for t in range(60):
                a = rng.integers(4) if rng.random() < 0.15 else int(np.argmax(Q[s]))
                n = move(s, a); r = -0.1
                for pr in [p for p in pending if p[0] == t]:
                    r += pr[1]; pending.remove(pr)
                if n == GOAL and first is None:
                    first = t + 1
                    if k == 0: r += 10.0
                    else: pending.append((t + k, 10.0))
                Q[s, a] += 0.5 * (r + 0.9 * Q[n].max() - Q[s, a])
                s = n
            steps_to.append(first if first else 60)
        last = np.mean(steps_to[-200:])
        rows.append((k, last, steps_to))
        print(f"   delay {k:2d} steps: mean steps to the first delivery, last 200 episodes = {last:5.1f}   (shortest possible 10; a random walk needs ~60)")
    print("   — nothing about the task changed; only *when* the signal arrived. A late reward lands on whatever the agent happened to be doing when it came.")
    np.savez(SCRATCH + "/delay.npz", **{f"k{k}": np.array(st) for k, l, st in rows})

# ------------------------------------------------------------ 3. extinction of helping
def part3():
    print("\n3. the helper — each round: help the neighbour (cost 1) or not (cost 0); does the neighbour reward help?")
    rng = np.random.default_rng(3)
    out = {}
    for name, reward_for_help, when in (("neighbour rewards help (+3)", 3.0, "always"),
                                        ("neighbour rewards help for 300 rounds, then stops", 3.0, "until300"),
                                        ("neighbour never rewards", 0.0, "always")):
        q = np.zeros(2); helps = []
        for t in range(1200):
            a = rng.integers(2) if rng.random() < 0.1 else int(np.argmax(q))     # 1 = help
            r = -1.0 if a == 1 else 0.0
            paying = reward_for_help if (when == "always" or t < 300) else 0.0
            if a == 1: r += paying
            q[a] += 0.1 * (r - q[a])
            helps.append(a)
        helps = np.array(helps); out[name] = helps
        w = lambda a, b: 100 * helps[a:b].mean()
        print(f"   {name:52s}: helping {w(0,100):4.0f}% in rounds 0–100, {w(250,300):4.0f}% at 250–300, {w(600,700):4.0f}% at 600–700, {w(1100,1200):4.0f}% at the end")
    print("   — help that is never rewarded is tried, found to cost, and dropped; help that stops being rewarded is dropped too. The neighbour's thanks is the signal that keeps it alive.")
    np.savez(SCRATCH + "/helper.npz", **{k.replace(" ", "_"): v for k, v in out.items()})

if __name__ == "__main__":
    part1(); part2(); part3()

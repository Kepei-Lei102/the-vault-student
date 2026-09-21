"""Privacy-Preserving Computation — six experiments you can run.

[[Data Protection and Privacy]] protects what comes OUT of a computation (anonymised tables, noisy totals).
This file is about the other half: doing the computation when nobody is allowed to see what goes IN.

1. secure_sum()       — three hospitals add their patient counts.  Each number is cut into random shares;
                        no party ever holds another's number; the total is exact.
2. shamir()           — a secret split into 5 shares so that ANY 3 rebuild it and any 2 learn nothing at all.
3. beaver_multiply()  — multiplying two shared numbers without opening either: the step from "sums" to
                        "any calculation".
4. paillier()         — arithmetic on ciphertexts.  Encrypt, add the ciphertexts' plaintexts by multiplying the
                        ciphertexts, decrypt the total.  An encrypted ballot box, and what it costs.
5. federated()        — ten clinics train one model without pooling their records; then a single
                        update is shown to leak a patient's record exactly; then secure aggregation hides it.
6. zero_knowledge()   — prove you know a secret number without revealing it; a cheat survives n rounds
                        with probability 2^-n (measured); transcripts can be forged afterwards, so they
                        convince nobody else: that is the "zero".

Run:  python3 privacy-preserving-computation-lab.py      (standard library + numpy, about 10 s)
Everything is a teaching toy: real systems use audited libraries, larger keys and authenticated channels.
"""
import math
import random
import secrets
import time

import numpy as np

rnd = random.Random(2026)
P = 2**61 - 1                      # a Mersenne prime: all share arithmetic is done modulo P


# ------------------------------------------------------------------ 1. additive secret sharing
def share(x, n, p=P):
    """Cut x into n numbers that add up to x (mod p).  Any n-1 of them are uniformly random."""
    parts = [secrets.randbelow(p) for _ in range(n - 1)]
    return parts + [(x - sum(parts)) % p]


def secure_sum(values=(1204, 877, 2310)):
    n = len(values)
    table = [share(v, n) for v in values]                 # row i: the shares hospital i deals out
    held = [[table[i][j] for i in range(n)] for j in range(n)]   # column j: what hospital j ends up holding
    partial = [sum(h) % P for h in held]                  # each hospital adds what it holds and announces that
    total = sum(partial) % P
    print(f"  private inputs {values};  announced partial sums {partial}")
    print(f"  total = {total}   (true total {sum(values)})")
    print(f"  hospital 0 sees of hospital 1's number only the share {held[0][1]}: a uniformly random 61-bit value")
    # is a single share independent of the secret?  Share two very different secrets many times and compare.
    a = np.array([share(5, 3)[0] / P for _ in range(20_000)]); b = np.array([share(2_000_000, 3)[0] / P for _ in range(20_000)])
    print(f"  mean of one share of the secret 5: {a.mean():.4f};  of the secret 2 000 000: {b.mean():.4f}  (both uniform on 0..1: no information)")
    print("  what still leaks: the OUTPUT.  If two hospitals collude they subtract their own numbers from the total and learn the third's.")


# ------------------------------------------------------------------ 2. Shamir threshold sharing
def shamir_split(secret, k, n, p=P):
    coeffs = [secret] + [secrets.randbelow(p) for _ in range(k - 1)]        # a random polynomial of degree k-1 with f(0) = secret
    return [(x, sum(c * pow(x, e, p) for e, c in enumerate(coeffs)) % p) for x in range(1, n + 1)]


def shamir_join(points, p=P):
    """Lagrange interpolation at x = 0."""
    total = 0
    for i, (xi, yi) in enumerate(points):
        num = den = 1
        for j, (xj, _) in enumerate(points):
            if i != j:
                num = num * (-xj) % p; den = den * (xi - xj) % p
        total = (total + yi * num * pow(den, -1, p)) % p
    return total


def shamir(secret=424242, k=3, n=5):
    pts = shamir_split(secret, k, n)
    print(f"  secret {secret} split into {n} shares, threshold {k}")
    for combo in ((0, 1, 2), (1, 3, 4), (0, 2, 4)):
        print(f"    shares {[c+1 for c in combo]} rebuild {shamir_join([pts[c] for c in combo])}")
    two = [pts[0], pts[1]]
    for guess in (0, 1, 999_999, secret):
        # with two real shares, ANY guessed secret is consistent with exactly one parabola
        implied = lagrange_at([(0, guess)] + two, 3)               # the parabola through (0, guess) and the two real shares
        print(f"    two shares + the guess {guess:>7}: consistent, implying share 3 would be {implied}")
    print("  every possible secret fits two shares equally well: two shares carry no information, not merely 'too little'")


def lagrange_at(points, x0, p=P):
    total = 0
    for i, (xi, yi) in enumerate(points):
        num = den = 1
        for j, (xj, _) in enumerate(points):
            if i != j:
                num = num * (x0 - xj) % p; den = den * (xi - xj) % p
        total = (total + yi * num * pow(den, -1, p)) % p
    return total


# ------------------------------------------------------------------ 3. multiplying shared values
def beaver_multiply(x=1234, y=5678, n=3):
    xs, ys = share(x, n), share(y, n)
    a, b = secrets.randbelow(P), secrets.randbelow(P)               # prepared in advance by a dealer, or by another protocol
    As, Bs, Cs = share(a, n), share(b, n), share(a * b % P, n)
    d = sum((xs[i] - As[i]) for i in range(n)) % P                  # opened in public: x - a, masked by the random a
    e = sum((ys[i] - Bs[i]) for i in range(n)) % P                  # opened in public: y - b
    zs = [(Cs[i] + d * Bs[i] + e * As[i] + (d * e if i == 0 else 0)) % P for i in range(n)]
    z = sum(zs) % P
    print(f"  shared x and y; opened only d = x-a = {d} and e = y-b = {e} (random-looking, because a and b are)")
    print(f"  product of the shares' secrets = {z}   (true {x*y})")
    print("  with + and x on shares, any calculation that can be written as a circuit can be run on data nobody sees")


# ------------------------------------------------------------------ 4. Paillier: additively homomorphic encryption
def is_prime(n, rounds=24):
    if n < 2:
        return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % q == 0:
            return n == q
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2; s += 1
    for _ in range(rounds):
        a = rnd.randrange(2, n - 1); x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def random_prime(bits):
    while True:
        c = rnd.getrandbits(bits) | (1 << (bits - 1)) | 1
        if is_prime(c):
            return c


class Paillier:
    def __init__(self, bits=512):
        p, q = random_prime(bits // 2), random_prime(bits // 2)
        self.n = p * q; self.n2 = self.n * self.n
        self.lam = math.lcm(p - 1, q - 1); self.mu = pow(self.lam, -1, self.n)

    def enc(self, m):
        r = secrets.randbelow(self.n - 2) + 1
        return (1 + m * self.n) * pow(r, self.n, self.n2) % self.n2           # (1+n)^m = 1 + mn  (mod n^2)

    def dec(self, c):
        return (pow(c, self.lam, self.n2) - 1) // self.n * self.mu % self.n

    def add(self, c1, c2):                 # Enc(a) * Enc(b) = Enc(a + b)
        return c1 * c2 % self.n2

    def times(self, c, k):                 # Enc(a) ^ k = Enc(k a)
        return pow(c, k, self.n2)


def paillier():
    t0 = time.perf_counter(); ph = Paillier(512); t_key = time.perf_counter() - t0
    a, b = 3500, 4200
    ca, cb = ph.enc(a), ph.enc(b)
    print(f"  key generated in {t_key:.2f} s (n has {ph.n.bit_length()} bits; real deployments use 2048 or more)")
    print(f"  Enc({a}) = {str(ca)[:28]}…  ({ca.bit_length()} bits);  encrypting {a} again gives a different ciphertext: {ph.enc(a) != ca}")
    print(f"  Dec( Enc({a}) * Enc({b}) ) = {ph.dec(ph.add(ca, cb))}     Dec( Enc({a}) ^ 12 ) = {ph.dec(ph.times(ca, 12))}")
    votes = [rnd.random() < 0.57 for _ in range(400)]
    t0 = time.perf_counter(); box = [ph.enc(int(v)) for v in votes]; t_enc = time.perf_counter() - t0
    t0 = time.perf_counter(); tally = 1
    for c in box:
        tally = ph.add(tally, c)
    t_add = time.perf_counter() - t0
    print(f"  400 encrypted ballots: the counting server multiplies ciphertexts and never sees a vote; decrypted tally {ph.dec(tally)} (true {sum(votes)})")
    t0 = time.perf_counter(); s = 0
    for v in votes * 250:
        s += v
    t_plain = (time.perf_counter() - t0) / 250
    print(f"  cost: encrypt {1e3*t_enc/400:.2f} ms per ballot; add {1e6*t_add/400:.1f} µs against {1e9*t_plain/400:.0f} ns in the clear "
          f"({t_add/t_plain:,.0f} x slower); each 1-bit vote occupies {box[0].bit_length()} bits")
    # RSA's homomorphism, for contrast
    p_, q_ = 61, 53; n_ = p_ * q_; e_ = 17; d_ = pow(e_, -1, (p_ - 1) * (q_ - 1))
    m1, m2 = 7, 12
    print(f"  textbook RSA is homomorphic for x: Enc(7)*Enc(12) decrypts to {pow(pow(m1, e_, n_) * pow(m2, e_, n_) % n_, d_, n_)} = 7*12. "
          "In RSA this is a weakness (forgeable messages) that padding removes; Paillier is built to keep it.")


# ------------------------------------------------------------------ 5. federated learning
def sigmoid(z):
    return 1 / (1 + np.exp(-np.clip(z, -60, 60)))


def train(X, y, w=None, epochs=200, lr=0.5):
    w = np.zeros(X.shape[1]) if w is None else w.copy()
    for _ in range(epochs):
        w -= lr * X.T @ (sigmoid(X @ w) - y) / len(y)
    return w


def accuracy(w, X, y):
    return float(((sigmoid(X @ w) > 0.5) == y).mean())


def federated(clients=10, per_client=30, d=20, rounds=40):
    g = np.random.default_rng(7)
    w_true = g.normal(0, 3.0, d + 1)

    def make(n, shift):
        X = g.normal(0, 1, (n, d)) + shift
        X = np.hstack([X, np.ones((n, 1))])
        y = (sigmoid(X @ w_true) > g.random(n)).astype(float)
        return X, y
    shifts = [g.normal(0, 0.8, d) for _ in range(clients)]          # every clinic sees a different kind of patient
    data = [make(per_client, s) for s in shifts]
    tests = [make(300, s_) for s_ in shifts]                        # unseen patients of the same ten kinds
    Xt = np.vstack([X for X, _ in tests]); yt = np.concatenate([y for _, y in tests])
    Xall = np.vstack([X for X, _ in data]); yall = np.concatenate([y for _, y in data])
    central = accuracy(train(Xall, yall, epochs=400), Xt, yt)
    alone = np.mean([accuracy(train(X, y, epochs=400), Xt, yt) for X, y in data])
    w = np.zeros(d + 1)
    for _ in range(rounds):                                         # FedAvg: the model travels, the data stays
        w = np.mean([train(X, y, w, epochs=10) for X, y in data], axis=0)
    fed = accuracy(w, Xt, yt)
    print(f"  accuracy on patients from all ten clinics:  each clinic alone {100*alone:.1f} %   federated {100*fed:.1f} %   all data pooled {100*central:.1f} %")
    # leakage: one patient's record from one gradient
    X, y = data[3]; x, label = X[17], y[17]
    err = sigmoid(x @ w) - label
    grad = err * x                                                  # what the clinic would upload after one step on this patient
    recovered = grad / grad[-1]                                     # the last feature is the constant 1, so grad[-1] = err
    print(f"  one patient's features      {np.round(x[:5], 3)} …")
    print(f"  rebuilt from the 'update'   {np.round(recovered[:5], 3)} …   max error {np.abs(recovered - x).max():.1e}")
    print("  'the data never leaves the device' is true of the bytes and false of the information")
    # secure aggregation with pairwise masks
    updates = [train(X, y, w, epochs=10) - w for X, y in data]
    masked = [u.copy() for u in updates]
    for i in range(clients):
        for j in range(i + 1, clients):
            m = g.normal(0, 100, d + 1)                             # agreed secretly by clinics i and j
            masked[i] += m; masked[j] -= m
    size = np.mean([np.linalg.norm(m_) / np.linalg.norm(u) for m_, u in zip(masked, updates)])
    corr = np.mean([abs(np.corrcoef(m_, u)[0, 1]) for m_, u in zip(masked, updates)])
    print(f"  with pairwise masks each upload is {size:,.0f} times larger than the true update and unrelated to it "
          f"(mean |correlation| {corr:.2f}, the value expected of pure noise in {d+1} dimensions is {np.sqrt(2/(np.pi*(d+1))):.2f});")
    print(f"  the masks cancel in the sum: the server's total differs from the true total by {np.abs(sum(masked) - sum(updates)).max():.1e}")
    return alone, fed, central, x, recovered


# ------------------------------------------------------------------ 6. zero-knowledge proof of knowledge
def safe_prime(bits=96):
    while True:
        q = random_prime(bits - 1); p = 2 * q + 1
        if is_prime(p):
            return p, q


def zero_knowledge(rounds_list=(1, 2, 4, 8, 12), trials=360_000):
    p, q = safe_prime(); gen = 4                                     # 4 = 2^2 generates the subgroup of prime order q
    x = secrets.randbelow(q); y = pow(gen, x, p)                     # y is public; x is the secret ("I know the password behind y")
    # one honest round
    r = secrets.randbelow(q); t = pow(gen, r, p); c = secrets.randbelow(2); s = (r + c * x) % q
    print(f"  public y = g^x mod p ({p.bit_length()}-bit p).  Round: commit t, challenge c = {c}, response s.  Check g^s == t * y^c: {pow(gen, s, p) == t * pow(y, c, p) % p}")
    # a cheat who does not know x must guess the challenge before committing
    y_inv = pow(y, -1, p)
    def cheat_round():
        guess = rnd.getrandbits(1); s_ = rnd.randrange(q)
        t_ = pow(gen, s_, p) * (y_inv if guess else 1) % p           # prepared so that the check passes IF c == guess
        c_ = rnd.getrandbits(1)
        return pow(gen, s_, p) == t_ * pow(y, c_, p) % p
    base = np.array([cheat_round() for _ in range(trials)])
    print(f"  a cheat passes one round with probability {base.mean():.3f}")
    out = {}
    for n in rounds_list:
        k = trials // n; passed = base[:k * n].reshape(k, n).all(axis=1).mean()
        out[n] = passed
        print(f"    {n:2d} rounds: passes {passed:.5f}   (2^-{n} = {2.0**-n:.5f})")
    print(f"  20 rounds: one in {2**20:,};  40 rounds: one in {2**40:,}")
    # the simulator: valid-looking transcripts WITHOUT the secret, by choosing the challenge first
    ok = all(pow(gen, s_, p) == t_ * pow(y, c_, p) % p
             for c_, s_, t_ in ((c_, s_, pow(gen, s_, p) * pow(y_inv, c_, p) % p) for c_, s_ in ((rnd.getrandbits(1), rnd.randrange(q)) for _ in range(1000))))
    print(f"  1000 forged transcripts (t, c, s) made without x all verify: {ok}.  A transcript therefore proves nothing to a bystander;")
    print("  only someone who chose the challenges live, after the commitment, is convinced.  Nothing about x can be in the transcript.")
    return out


if __name__ == "__main__":
    for i, f in enumerate((secure_sum, shamir, beaver_multiply, paillier, federated, zero_knowledge), 1):
        print(f"\n{i}. {f.__name__.replace('_', ' ')}"); f()
